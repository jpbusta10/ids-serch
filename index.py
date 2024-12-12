import requests 

import pandas as pd

ids = ids = ["5ef1b7549e282010f8a4230c", "5ef1b7549e282010f8a4230d", "5ef1b7549e282010f8a4230e", "5ef1b7549e282010f8a4230f", "5ef1b7549e282010f8a42310",
             "5ef1b7549e282010f8a42313", "5ef1b7549e282010f8a42314", "5ef1b7549e282010f8a42315", "5ef1b7549e282010f8a42316", "5ef1d3c79e282010f8a425ba", 
             "5ef1d3c79e282010f8a425bb", "5ee00d519e282010f8a1cefe", "5ee00d519e282010f8a1cf35", "5ef146489e282010f8a40dd2", "5ef19b249e282010f8a420ba", 
             "5ef19b249e282010f8a420c4", "5ef19b249e282010f8a420d3", "5f923b4a9e282010f8b77245", "5feeafcf9e282010f8c395d2", "62bf1bff149e1cced8c1c11d", 
             "62bfe114149e1cced8c1d1c0", "62d6f9c8149e1cced8c47de9", "63117bd9149e1cced8ca1b75", "631a484b149e1cced8cadf9b", "632975b3149e1cced8cc14f7", 
             "63325e54149e1cced8ccdf16", "63325e54149e1cced8ccdf17", "63325e54149e1cced8ccdf18", "63325e54149e1cced8ccdf19", "63325e54149e1cced8ccdf1e", 
             "63325e54149e1cced8ccdf21", "634734aca4cc292e2f41768d", "6348bed0a4cc292e2f419dfe", "635f40fba4cc292e2f437d14", "635f40fba4cc292e2f437d15", 
             "635f40fba4cc292e2f437d16", "63617409a4cc292e2f43a741", "63617409a4cc292e2f43a742", "63617409a4cc292e2f43a745", "63617409a4cc292e2f43a746", 
             "636433eba4cc292e2f43de6c", "63653149a4cc292e2f43f16b", "63656997a4cc292e2f43f959", "63656997a4cc292e2f43f95a", "63656997a4cc292e2f43f95b", 
             "6365a1e6a4cc292e2f43ff90", "6365a1e6a4cc292e2f43ff91", "6365a1e6a4cc292e2f43ff92", "6365a1e6a4cc292e2f43ff96", "6365a1e6a4cc292e2f43ff97", 
             "6365da39a4cc292e2f4403cc", "6365da39a4cc292e2f4403cd", "6365da39a4cc292e2f4403ce", "6365da39a4cc292e2f4403cf", "6365da39a4cc292e2f4403d0", 
             "636942fea4cc292e2f443891", "636942fea4cc292e2f443892", "638846eaa4cc292e2f467717", "638846eaa4cc292e2f467718", "63a961cca4cc292e2f491f66", 
             "63a961cca4cc292e2f491f67", "63a961cca4cc292e2f491f68", "63a961cca4cc292e2f491f69", "63b11498a4cc292e2f49a597", "63b11498a4cc292e2f49a598", 
             "63b11498a4cc292e2f49a599", "63b11498a4cc292e2f49a59a", "6552e3b873fec95dc8d1404f", "6559c07673fec95dc8d1d1e0", "655ef30d73fec95dc8d23d0f", 
             "656595b973fec95dc8d2bc09", "65683d3d73fec95dc8d2f702", "656a574173fec95dc8d326e6", "656c1c6d73fec95dc8d34607", "6570c1cb73fec95dc8d3c4fc", 
             "657d427173fec95dc8d4c976", "6584c90f73fec95dc8d567b4", "659e3b9673fec95dc8d734d0", "65a7865a73fec95dc8d7cf81", "65bf32e873fec95dc8d97200", 
             "65deda0173fec95dc8daf6ce", "65e1725773fec95dc8db0f22", "65e2ff0973fec95dc8db18f3", "65e2ff0973fec95dc8db18f4", "65e2ff0973fec95dc8db18f5", 
             "65e2ff0973fec95dc8db18f6", "65e9689f73fec95dc8db4278", "65e9689f73fec95dc8db4279", "65e9689f73fec95dc8db427a", "65e9689f73fec95dc8db427b", 
             "65e9689f73fec95dc8db427c", "65f2a32173fec95dc8db7d94", "65f2a32173fec95dc8db7d95", "65f2a32173fec95dc8db7d96", "65f2a32173fec95dc8db7d97", 
             "660518d073fec95dc8dbee95", "660e470973fec95dc8dc1d70", "660e470973fec95dc8dc1d71", "660e470973fec95dc8dc1d72", "660e470973fec95dc8dc1d73", 
             "660e470973fec95dc8dc1d74", "6617768f73fec95dc8dc7d69", "6617768f73fec95dc8dc7d6a", "6617930273fec95dc8dc7fd9", "6617930273fec95dc8dc7fda", 
             "6617930273fec95dc8dc7fdb", "6617930273fec95dc8dc7fdc", "6617930273fec95dc8dc7fdd", "6617930273fec95dc8dc7fde", "6617930273fec95dc8dc7fdf", 
             "6618918d73fec95dc8dc8e9e", "66333c9a73fec95dc8dd29c9", "66333c9a73fec95dc8dd29ca", "663c71fe73fec95dc8dd54e9", "6645aa8b73fec95dc8dd8532", 
             "6645aa8b73fec95dc8dd8534", "6648592e73fec95dc8dd98a9", "664ee4da73fec95dc8ddc06f", "665041ba73fec95dc8ddcb0f", "6651969573fec95dc8ddd112", "665821a173fec95dc8ddee41", "665821a173fec95dc8ddee42", "666104f073fec95dc8de19bb", "66615a0373fec95dc8de1b48", "66615a0373fec95dc8de1b49", "6677a65173fec95dc8df01ea", "6698b8d073fec95dc8dfee3f", "66a73f7d73fec95dc8e03e81", "66b0912673fec95dc8e0fa12", "66e3e14e73fec95dc8e2b3bf", "66e3e14e73fec95dc8e2b3c0", "66e3e14e73fec95dc8e2b3c1", "66e3e14e73fec95dc8e2b3c2", "66e3e14e73fec95dc8e2b3c3", "66e3e14e73fec95dc8e2b3c4", "66e3e14e73fec95dc8e2b3c5", "66e3e14e73fec95dc8e2b3c6", "66e6885973fec95dc8e2bfa5", "66ea11af73fec95dc8e2dd74", "66ea11af73fec95dc8e2dd75", "66eb49a073fec95dc8e2ea46", "66eb49a073fec95dc8e2ea47", "66f6597973fec95dc8e328ca", "66f6597973fec95dc8e328cb", "66f6597973fec95dc8e328cc", "66f6597973fec95dc8e328cd", "66f6597973fec95dc8e328ce", "66f6597973fec95dc8e328cf", "66f6597973fec95dc8e328d0", "66f6597973fec95dc8e328d1", "66fba8f073fec95dc8e356c5", "66fcfcbf73fec95dc8e371d0", "66fe1ab673fec95dc8e37e5b", "66fe372873fec95dc8e37f03", "66ff8b4773fec95dc8e38798", "670a28d473fec95dc8e3dea6", "6710ae5d73fec95dc8e3fe71", "673057c073fec95dc8e48951", "6732f88a73fec95dc8e4922b", "6735a19f73fec95dc8e4a337", "673ed82d73fec95dc8e4de11", "674c14de73fec95dc8e528df", "674d68c273fec95dc8e52ee4", "675148f473fec95dc8e576af", "627b1f71149e1cced8bb3048", "627c55fc149e1cced8bb8b75", "627ec31f149e1cced8bbbf30", "627edf60149e1cced8bbc2c9", "62967869149e1cced8be0235", "62a12782149e1cced8bf0ebc", "62ae46d9149e1cced8c0325c", "62cdb6bd149e1cced8c3af2f", "62cf4252149e1cced8c3d58e", "62cf7ae2149e1cced8c3df26", "62d0790c149e1cced8c3f4f9", "62df4251149e1cced8c53ecf", "62f2ae16149e1cced8c6ffb5", "63068b82149e1cced8c8a1c1", "63291847149e1cced8cc0dff", "633b30d4a4cc292e2f406e64", "633d1682a4cc292e2f40a2e9", "63506af2a4cc292e2f422dc5", "63659d25a4cc292e2f43fe98", "637430fda4cc292e2f450e29", "638a9a29a4cc292e2f46a37e", "639d0d85a4cc292e2f484672", "63bf94e7a4cc292e2f4ae571", "63cb2287a4cc292e2f4bc0e9", "63fe995ca4cc292e2f50e154", "63fed1e6a4cc292e2f50e7db", "63fed1e6a4cc292e2f50e7e0", "640d82e8a4cc292e2f523f69", "644af0f73b08e72840d29934", "645312993b08e72840d31c89", "645312993b08e72840d31c8a", "6455bd773b08e72840d37b53", "6455bd773b08e72840d37b54", "6455bd773b08e72840d37b56", "645d4f9f3b08e72840d42bfd", "645fdd103b08e72840d45be8", "6477a6aa3b08e72840d698f0", "647d647d3b08e72840d7058a", "649cdab03b08e72840d9a38c", "649cdab03b08e72840d9a38d", "649cdab03b08e72840d9a38e", "649f819b3b08e72840d9e2bb", "649f819b3b08e72840d9e2bc", "649f819b3b08e72840d9e2bd", "649f819b3b08e72840d9e2be", "649f819b3b08e72840d9e2bf", "649f819b3b08e72840d9e2c1", "64a607843b08e72840da7a21", "64af9ba33b08e72840db3ab7", "64b348803b08e72840db7c70", "64db23683b08e72840de77a8", "64dc67213b08e72840de93ab", "65337d3d73fec95dc8cf1083", "6538af9873fec95dc8cf64a7", "653b649173fec95dc8cf97f9", "6541ebb773fec95dc8d007ed", "65449f1373fec95dc8d03a49", "654746b573fec95dc8d06593", "625f097c149e1cced8b7e252", "625f097c149e1cced8b7e253", "625f097c149e1cced8b7e254", "625f097c149e1cced8b7e255", "625f097c149e1cced8b7e25d", "625f097c149e1cced8b7e25f", "625f097c149e1cced8b7e261", "625f097c149e1cced8b7e263", "625f097c149e1cced8b7e264", "625f097c149e1cced8b7e268", "625f097c149e1cced8b7e2dd", "625f097c149e1cced8b7e2e0", "625f097c149e1cced8b7ec3b", "625f097c149e1cced8b7ec72", "625f097c149e1cced8b7ec8a", "625f097c149e1cced8b7ec8c", "625f097c149e1cced8b7ec8e", "625f097c149e1cced8b7ec90", "625f097c149e1cced8b7ec92", "625f097c149e1cced8b7ec94", "625f097c149e1cced8b7ec99", "625f097c149e1cced8b7ec9b", "625f097c149e1cced8b7eca5", "625f097c149e1cced8b7eca6", "625f097c149e1cced8b7eca8", "625f097c149e1cced8b7ecaa", "625f097c149e1cced8b7ecac", "625f097c149e1cced8b7ecaf", "625f097c149e1cced8b7ecb3", "625f097c149e1cced8b7ecb5", "625f097c149e1cced8b7ecb6", "625f097c149e1cced8b7ecb9", "625f097c149e1cced8b7ecbb", "625f097c149e1cced8b7ecbd", "625f097c149e1cced8b7ecbe", "625f097c149e1cced8b7ecc0", "625f097c149e1cced8b7ecc2", "625f097c149e1cced8b7ecc3", "625f097c149e1cced8b7ecdc", "625f097c149e1cced8b7ecde", "625f097c149e1cced8b7ece0", "625f097c149e1cced8b7ece2", "625f097c149e1cced8b7ece3", "625f097c149e1cced8b7ece5", "625f097c149e1cced8b7ece7", "625f097c149e1cced8b7ece9", "625f097c149e1cced8b7ecea", "625f097c149e1cced8b7ecee", "625f097d149e1cced8b7ef68", "625f097d149e1cced8b7efac", "6269eb3a149e1cced8b9586d", "6271bf11149e1cced8ba0db5"]
def getContents():
    url = f"https://unity-content.tbxapis.com/v1/batch/dsh_demo/shown?key=abd3912eb2100a732cd6a3788e1d8c42&secret=d8dd6d4d748909468e45eb5644101876"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("status: 200")
            data = response.json()
            return data
        else:
            print(f"API request with status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
    return 'Unknown'

data = getContents()
matched_items = []
not_matched = []
if data:
    for content in data:
        content_id = content.get("id")
        if content_id in ids:
            matched_items.append({
                "id": content_id,
                "externalId": content.get("externalId")
            })
        else:
            not_matched.append({
                "id": content_id
            })

if matched_items: 
    df = pd.DataFrame(matched_items)
    df.to_csv("matched_ids.csv", index=False)
    print(f"matched saved in matched_ids.csv  ({len(matched_items)} matched ids)")

if not_matched: 
    df_not_matched = pd.DataFrame(not_matched)
    df_not_matched.to_csv("not_matched_ids.csv", index=False)
    print(f"Data not matched saved in not_matched_ids.csv ({len(not_matched)} not matched)")

if not matched_items:
    print("No matched ids")

if not not_matched: 
    print("every id matched")

