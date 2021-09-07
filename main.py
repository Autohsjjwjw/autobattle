
poke_list = ['Yveltal']

poke_list2 = ['Found!', '', 'Ninjask', 'Aerodactyl', '', '', 'Mewtwo', 'Mew', 'Deoxys', '', 'Groudon', 'Kyogre', 'Rayquaza', '', 'Diancie', 'Slaking', 'Dialga',
 'Palkia', 'Arceus', 'Regigigas', 'Darkrai', 'Cressellia', 'Giratina', '', '', 'Reshiram', 'Zekrom', 'Kyurem', 'Landorus', 'Thundurus', 'Tornadus', 'Meloetta', 'Greninja',
 'Xerneas', 'Yveltal', 'Zygarde', 'Hoopa', 'Cosmog', 'Cosmoem', 'Solgaleo', 'Lunala', 'Necrozma', 'Magearna', 'Marshadow', 'Pheromosa', 'Poipole', 'Naganadel',
 'Zeraora', 'Pheromosa', 'Sylveon', 'Metagross']

#Thanks Anil Vro
with TelegramClient(StringSession(SESSION_KEY), API_ID, API_HASH,) as client:


    @client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "hexamatch (.*) (\w+)"))
    async def hexamatch(event):
        bid = 572621020
        msg = "?eval async for x in bot.iter_messages(\"@jsjwjxjjdjwiwdsk\", limit=5):\n await x.click(0)"
        times_hunt = event.pattern_match.group(1)
        set_sec = event.pattern_match.group(2)
        eta = int((int(times_hunt) * int(set_sec))/60)
        if not times_hunt.isnumeric():
            text = "`Onii-sama nHunts and nSex both must be integers :)`"
            await event.edit(text)
        else:
            await event.edit(
                        f"\n\n`Hunts: {times_hunt}. Duration: {set_sec} seconds.`"
                        f"\n\n`Targeted Hunt.`"
                        f"\n\n`ETA: {eta} minutes.`")
            async with client.conversation('Hexamonbot') as conv:
                for i in range(int(times_hunt)):
                    await conv.send_message('/hunt')
                    if int(i) == int(times_hunt)-1:
                        await event.reply("`Hunting complete.`")
                    else:
                        poke_r = await conv.get_response()
                        get_res_msg = poke_r.text.split(" ")
                        get_poke_n = get_res_msg[2].replace("**","") 
                        
                        if get_poke_n in poke_list:
                            print(f'In list: {get_poke_n}')
                            await event.reply(f"Master, {get_poke_n} has appeared. Let\'s catch it.")  
                            break
                        else:
                            time.sleep(int(set_sec))
        
    @client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "hexa (.*) (\w+)"))
    async def hexa(event):
        bid = 572621020
        msg = "?eval async for x in bot.iter_messages(\"@jsjwjxjjdjwiwdsk\", limit=5):\n await x.click(0)"
        times_hunt = event.pattern_match.group(1)
        set_sec = event.pattern_match.group(2)
        eta = int((int(times_hunt) * int(set_sec))/80)
        if not times_hunt.isnumeric():
            text = "`Onii-sama nHunts and nSex both must be integers :)`"
            await event.edit(text)
        else:
            await event.edit(
                        f"\n\n`Hunts: {times_hunt}. Duration: {set_sec} seconds.`"
                        f"\n\n`Normal Hunt.`"
                        f"\n\n`ETA: {eta} minutes.`")
            for i in range(int(times_hunt)):
                await client.send_message(bid,msg)
                if int(i) == int(times_hunt)-1:
                    await event.reply("`Hunting complete.`")
                else:
                    time.sleep(int(set_sec))

    @client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "list"))
    async def list(event):
        await event.reply(f"`{poke_list}`")

    @client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "restart"))
    async def shutdown_handler(event):
        CMD = CMD_PREFIX[1:]
        await event.edit(f"**Restarted.**")
        await client.disconnect()
        
    client.run_until_disconnected()
