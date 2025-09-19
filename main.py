import asyncio
import discord
from discord.ext import commands
from config import token
import sql

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='-', intents=intents)

@client.event
async def on_ready():
    print(f'Giriş yaptı:  {client.user}')

@client.event
async def on_message(message):
     if message.author == client.user:
        return
    
     #SSS Soru Cevap Kod
     if message.content.lower().startswith("-nasıl alışveriş yapabilirim"):
            await message.channel.send('Alışveriş yapmak için, ilgilendiğiniz ürünü seçip "Alışveriş Sepetine Ekle" butonuna tıklayın. Ardından Alışveriş Sepetine gidin ve satın alma işlemini tamamlamak için yönergeleri takip edin.')

     if message.content.lower().startswith("-siparişimin durumunu nasıl öğrenebilirim"):
         await message.channel.send('Siparişinizin durumunu öğrenmek için internet sitemizdeki hesabınıza giriş yapın ve "Siparişlerim" bölümüne gidin. Orada, siparişinizin mevcut durumunu görebilirsiniz.')
    
     if message.content.lower().startswith("-bir siparişi nasıl iptal edebilirim"):
         await message.channel.send('Siparişinizi iptal etmek istiyorsanız, lütfen en kısa sürede müşteri hizmetlerimizle iletişime geçin. Siparişiniz gönderilmeden önce iptal işleminizde size yardımcı olmaya çalışacağız.') 

     if message.content.lower().startswith("-siparişim hasarlı gelirse ne yapmalıyım"):
         await message.channel.send('Hasarlı bir ürün aldıysanız, lütfen hemen müşteri hizmetlerimizle iletişime geçin ve hasarın fotoğraflarını sağlayın. Ürünü değiştirmeniz veya iade etmeniz konusunda size yardımcı olacağız.')

     if message.content.lower().startswith("-teknik destekle nasıl iletişime geçebilirim"):
         await message.channel.send('Teknik destekle, internet sitemizde yer alan telefon numarasını arayarak iletişime geçebilirsiniz. Alternatif olarak, sohbet robotumuz üzerinden de bizimle iletişim kurabilirsiniz.')

     if message.content.lower().startswith("-ödeme sırasında teslimat yöntemini değiştirebilir miyim"):
         await message.channel.send('Evet, ödeme sayfasında teslimat bilgilerini değiştirebilirsiniz. Kullanılabilir teslimat yöntemleri ve şartları orada listelenecektir.')





     if message.content.lower().startswith("-destekforum"):
          await message.channel.send("Lütfen sormak istediğiniz soruyu belirtin.")

          def check(m):
               return m.author == message.author and m.channel == message.channel

          try:

               user_question_message = await client.wait_for('message', check=check, timeout=60.0)
               user_question = user_question_message.content
               username = str(message.author) 
               sql.insert_question(username, user_question)

               await message.channel.send(f"Sorunuz başarıyla kaydedildi, **{username}**! en kısa sürede yetkili biri size dönüş sağlayacaktır.")

          except asyncio.TimeoutError:
               await message.channel.send("İşlem zaman aşımına uğradı. Lütfen daha sonra tekrar deneyin.")
     

     await client.process_commands(message)


client.run(token)