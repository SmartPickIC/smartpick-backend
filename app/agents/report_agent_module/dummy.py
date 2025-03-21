
#def get_review_data_dummy(product_name, total_reviews, positive_ratio, negative_ratio, positive_analysis, negative_analysis, selected_positive, selected_negative):
#    general_users = {
#        "product_name": product_name, # str
#        "total_reviews": total_reviews, # int
#        "positive_percentage": round(positive_ratio, 0), # int
#        "negative_percentage": round(negative_ratio, 0), # int
#        "positive_reviews": {
#            "key_points": positive_analysis["key_points"], # list
#            "reviews": [
#                {
#                    "text": review["text"],
#                    "platform": review["platform"]
#                }
#                for review in selected_positive
#            ] # list 안에 'text', 'platform' 키를 가진 딕셔너리들이 있음
#        },
#        "negative_reviews": {
#            "key_points": negative_analysis["key_points"],
#            "reviews": [
#                {
#                    "text": review["text"],
#                    "platform": review["platform"]
#                }
#                for review in selected_negative
#            ] # list 안에 'text', 'platform' 키를 가진 딕셔너리들이 있음
#        }
#    }
#    return general_users


def get_specification_data_dummy():
    test_set = {'제품명':'APPLE 2024 iPad mini A17 Pro 7세대', 
    '가격': 749000, 
        '추천 이유': {'pros': ['장점 1', '장점 2', '장점 3'], 'cons': ['단점 1', '단점 2', '단점 3']}, 
            '핵심 사항': [{'항목': 'AI', '사양': '요약편집교정, 이미지 생성편집, 음성비서', '설명': '다양한 AI 기능으로 작업을 효율적으로 지원합니다.'}, 
                    {'항목': '규격', ' 사양': '가로: 134.8mm, 세로: 195.4mm, 두께: 6.3mm, 무게: 293g, 출시가: 749,000원', '설명': '작고 가벼운 디자인으로 휴대성이 뛰어납니다.'}, 
                    {'항목': '네트워크', '사양': 'Wi-Fi전용, 802.11ax(Wi-Fi 6E), 듀얼밴드, 블루투스v5.3', '설명': '최신 Wi-Fi 기술로 빠르고 안정적인 연결을 제공합니다.'}, 
                    {'항목': '배터리', '사양': '충전단자: C타입, USB3.0, 약 5,078mAh(19.3WH), 최대충전: 약20W', '설명': '오랜 사용 시간을 제공하며 빠른 충전이 가 능합니다.'}, 
                    {'항목': '벤치마크', '사양': 'AP싱글코어: 2953, AP멀티코어: 7441', '설명': '우수한 성능으로 다 양한 작업을 원활하게 처리합니다.'}, 
                    {'항목': '사운드', '사양': '스피커: 2개, 마이크: 2개', '설명': '양질의  오디오 경험을 제공합니다.'}, 
                    {'항목': '시스템', '사양': 'A17 Pro, 6코어, 램: 8GB, 용량: 128GB, microSD미지원', '설명': '최신 A17 Pro 칩으로 뛰어난 성능을 자랑합니다.'}, 
                    {'항목': '카메라', '사양': '후면: 1,200만화소, 전면: 1,200만화소, 4K@60fps, F1.8, 센터 스테이지, 슬로모션 동영상', '설명': '고화질 사진과 동영상 촬영이 가 능합니다.'
                }
        ]
    }
    return test_set

def get_review_data_dummy(product_name, total_reviews, positive_ratio, negative_ratio, positive_analysis, negative_analysis, selected_positive, selected_negative):
    general_users = {
        "product_name": product_name, # str
        "total_reviews": total_reviews, # int
        "positive_percentage": round(positive_ratio, 0), # int
        "negative_percentage": round(negative_ratio, 0), # int
        "positive_reviews": {
            "key_points": positive_analysis,
            "reviews": selected_positive,
        },
        "negative_reviews": {
            "key_points": negative_analysis,
            "reviews": selected_negative
        }
    }
    return general_users
def get_review_data_real_dummy():
    product_name="아이패드 프로"
    total_reviews="1363"
    positive_ratio=89
    negative_ratio=11
    positive_analysis=["디자인 예뻐요", "영상 볼 때 최고", "배터리 오래가요"]
    negative_analysis=["애플펜슬 문제", "가격 비쌈", "주사율 아쉬움"]
    selected_positive=[]
    selected_negative=[]
    selected_positive.append({"text":"디자인은 예쁘고 색도 너무 잘나왔어요.", "platfotm":"쿠팡"})
    selected_positive.append({"text":"애플펜슬 너무 좋아요", "platfotm":"다나와"})
    selected_positive.append({"text":"이번이 정말 역대급인거 같아요", "platfotm":"쿠팡"})
    selected_negative.append({"text":"가격이 너무 비싸요 이러다 알바하다 죽겟어요", "platfotm":"다나와"})
    selected_negative.append({"text":"애플펜슬 2세대 바뀐것도 없으면서 비싸지기만 했어요", "platfotm":"네이버"})
    selected_negative.append({"text":"주사율 때문에 강제로 프로삿어요 전 프로싫은데", "platfotm":"다나와"})
    general_users = {
        "product_name": product_name, # str
        "total_reviews": total_reviews, # int
        "positive_percentage": round(positive_ratio, 0), # int
        "negative_percentage": round(negative_ratio, 0), # int
        "positive_reviews": {
            "key_points": positive_analysis,
            "reviews": selected_positive,
        },
        "negative_reviews": {
            "key_points": negative_analysis,
            "reviews": selected_negative
        }
    }
    return general_users



def get_youtube_data_dummy():
    
    dummy={}
    dummy['youtube']={}
    dummy['youtube']["query"]='애플의 아이패드 디지털 드로잉에 적합한 제품 리뷰 영상이 필요합니다. 우수한 펜 반응속도와 고급형 프로세서를 탑재한 제품에 관한 정보가 포함된 클립이 있으면 좋겠으며 예산은 100만원입니다. 이 영상에서는 해당 제품의 기능 요약 및 인상적인 장면, 사용자 리뷰 등의 정보를 제공해주길 원합니다.'
    dummy['youtube']["llm_process_data"]={}
    dummy['youtube']['raw_meta_data']={}
    dummy['youtube']["llm_process_data"]['자막요약']=[['이 영상은 아이패드 프로의 리뷰 영상으로, 저자는 이 제품을 구입한 후 사용하면서 느낀 점을 솔직하게 공유하고 있습니다. 아이패드의 화면, 성능, 디자인...를 설명하고, 휴대성과 내구성, 배터리 성능 등 다양한 측면에서 평가합니다.']]
    dummy['youtube']["llm_process_data"]['코드']=[['메인프롬프트확인', '태그=True', '예시확인']]
    dummy['youtube']["llm_process_data"]['timestamps']=['00:05:33', '00:02:15', '00:06:37', '00:17:33', '00:15:33']
    dummy['youtube']["llm_process_data"]['timestampsdiscriptions']=['05:33:아이패드프로에서 뉴진스 직캠을 보는 방법 설명', '02:15:디스플레이 후기 제공', '06:37:매직키보드에 대한 설명 진행', '17:33:전체 성능 요약 및 평가', '15:33:배터리 관련 내용 안내']
    dummy['youtube']["llm_process_data"]['seconds']=['1593']
    dummy['youtube']["llm_process_data"]['descriptions']=['아이패드 프로에 대한 디스플레이, 성능 및 배터리 등 주요 기능과 사용 후기를 전달합니다.', '전체 자막 요약: 비싼 만큼 좋을지, 디스플레이 성능 및 매직 키보드 사용 감, 애플 펜슬과 내구성, 스피커 및 배터리에 대한 리뷰가 포함되어 있습니다.']
    dummy['youtube']["llm_process_data"]['codes']=['역할확인', '세부규칙확인', '주의사항확인', '추가자료확인']
    dummy['youtube']["llm_process_data"]['clip']='https://www.youtube.com/watch?v=lCo2_4Qwjdo&t=1593'
    dummy['youtube']['raw_meta_data']['링크']='https://www.youtube.com/watch?v=zkDlswmkyLE'
    dummy['youtube']['raw_meta_data']['태그']=[['애플', '펜슬', 'USBC', '타블렛 액세서리', '리뷰']]
    dummy['youtube']['raw_meta_data']['조회수']='307K views'
    dummy['youtube']['raw_meta_data']['제목']='막 나가는(?) 애플의 11만 9천원짜리 애플 펜슬 USB-C 사 왔습니다'
    dummy['youtube']['raw_meta_data']['유튜버']='UNDERkg'
    dummy['youtube']['raw_meta_data']['업로드일']='1 year ago'
    dummy['youtube']['raw_meta_data']['설명']='펜슬 2의 염가판이라기 보다는 크레용의 개선판, 그러니까 럭키 짭플펜슬에 가까운 물건인데 가격은 119,000원 씩이나 하죠.더블 탭이나 무료 각인은 그러려니 하겠는데 필압 지원이 안 되는게 치명적인 단점.굳이 따지자면 호버가 되긴 하는데, 호버 되는 그 비싼 기종에서 7만원 아끼자고 이걸 사진 않을 테니...근데 써 보니까 마감도 좋고, 무게 균형도 정품 답고, 무엇보다 굿노트에서 필압 비스무리 한 것을 해 주긴 합니다. 정확한 원리는 모르겠지만 아마 속도 인식 같고, 애플 펜슬과 크레용만 정식 지원하니 뭔가 하는 듯. 00:00  - 인트로 00:08  - 인사 01:10  - 개봉 02:46  - 비교 04:18  - 설정 05:13  - 필기 06:09  - 그럼에도 불구하고 07:55  - 정리-페이스북    / underkg   -인스타그램    / underkgshow  '
    dummy['youtube']['raw_meta_data']['자막']='1\n00:00:00,040 --> 00:00:06,200\n옆에 착 달라붙어요 왜 안 또 먹아\n\n2\n00:00:02,480 --> 00:00:06,200\n아 맞다 이거 붙어가지고 페어리가 안\n\n3\n00:00:07,559 --> 00:00:12,759\n되지 안녕하세요 니입니다 오늘은\n\n4\n00:00:10,440 --> 00:00:14,920\n애플의 황당한 제품을 가져왔습니다\n\n5\n00:00:12,759 --> 00:00:17,320\n애플 펜슬 괄호 요구 usb-c 괄호\n\n6\n00:00:14,920 --> 00:00:19,359\n닫고 자이 제품이 뭔가에 대해서\n\n7\n00:00:17,320 --> 00:00:21,480\n간단하다면 간단하고 복잡하면 복잡해요\n\n8\n00:00:19,359 --> 00:00:23,599\n자 간단한 버전이 있어 럭키 자플\n\n9\n00:00:21,480 --> 00:00:25,480\n펜슬이다 자플 펜슬이 최근에 굉장히\n\n10\n00:00:23,599 --> 00:00:27,760\n발전을 했어요 처음에는 그냥 로지텍\n\n11\n00:00:25,480 --> 00:00:29,080\n크레용의 역 공학 버전 리버스\n\n12\n00:00:27,760 --> 00:00:31,000\n엔지니어링 버전으로 나와 가지고\n\n13\n00:00:29,080 --> 00:00:32,559\n꽁다리를 눌러 지 켜져야 된다든지\n\n14\n00:00:31,000 --> 00:00:34,320\n충전 단자에 끼워서 충전을 해야\n\n15\n00:00:32,559 --> 00:00:36,360\n된다든지 하는 살짝의 불편함이\n\n16\n00:00:34,320 --> 00:00:37,800\n있었는데 막 요즘은 옆에 붙고 충전\n\n17\n00:00:36,360 --> 00:00:40,200\n아이콘에 퍼센티지 뜨고 난리납니다\n\n18\n00:00:37,800 --> 00:00:42,120\n그렇다면 이것은 왜 럭키 하느냐 애플\n\n19\n00:00:40,200 --> 00:00:44,520\n딱지가 붙어 있다 뒤쪽에 애플 펜슬\n\n20\n00:00:42,120 --> 00:00:46,600\n괄로고 usb-c 괄호 닫고 돼 있고\n\n21\n00:00:44,520 --> 00:00:48,719\n충전을 어떻게 하느냐 요렇게 멋지게\n\n22\n00:00:46,600 --> 00:00:50,239\n한다 케이블을 연결하고 펜슬을 쏙\n\n23\n00:00:48,719 --> 00:00:52,199\n당기면 USB C 포트가 나오니까\n\n24\n00:00:50,239 --> 00:00:55,000\n거기다 끼워서 유선으로 열심히 충전을\n\n25\n00:00:52,199 --> 00:00:56,879\n하세요라고 그림이 있고 매력 포인트는\n\n26\n00:00:55,000 --> 00:00:58,280\n무엇이냐 usbc 케이블로 페어링 및\n\n27\n00:00:56,879 --> 00:01:00,160\n충전 아이패드의 자석으로 부착하여\n\n28\n00:00:58,280 --> 00:01:01,920\n보고한 대체 가능한 팁이다 그래서\n\n29\n00:01:00,160 --> 00:01:03,680\n이걸 어디다 쓰냐 usbc 커넥터가\n\n30\n00:01:01,920 --> 00:01:06,119\n있고 최신 버전에 아패드가 설치된\n\n31\n00:01:03,680 --> 00:01:07,920\n아이패드 모델에 쓰시면 된다라는 건데\n\n32\n00:01:06,119 --> 00:01:09,400\n사실 요거를 사야 될 아이패드는 딱\n\n33\n00:01:07,920 --> 00:01:11,360\n정해져 있다고 보시면 됩니다 제가\n\n34\n00:01:09,400 --> 00:01:14,000\n뜯으면서 설명을 드릴게요 자 요쪽에\n\n35\n00:01:11,360 --> 00:01:17,080\n환경이기 때문에 종이로 실이 있죠 쓱\n\n36\n00:01:14,000 --> 00:01:19,079\n잘라서 깔끔하게 떨어지네 샥 당겨서\n\n37\n00:01:17,080 --> 00:01:21,640\n보면은 디자인 바 애플린 캘리포니아\n\n38\n00:01:19,079 --> 00:01:23,960\n메이드인 차이나네요 굳이이 얘기를\n\n39\n00:01:21,640 --> 00:01:26,119\n하는 이유는 내년 아이폰은 인도에서\n\n40\n00:01:23,960 --> 00:01:28,640\n애초에 만들 거라는 소문이 돌고\n\n41\n00:01:26,119 --> 00:01:30,280\n있어요 사실 중국에서 상당히 많은\n\n42\n00:01:28,640 --> 00:01:31,840\n저기이 공장들이 나가고 있어요 뭐\n\n43\n00:01:30,280 --> 00:01:33,880\n갤럭시 같은 경우에도 베트남에 되게\n\n44\n00:01:31,840 --> 00:01:36,000\n큰 생산 기지가 있고 애플도 타일\n\n45\n00:01:33,880 --> 00:01:37,799\n중국해 가지고 입 인도를 하고 있는\n\n46\n00:01:36,000 --> 00:01:40,280\n분위기기 때문에 한번 봤어요 안쪽에\n\n47\n00:01:37,799 --> 00:01:42,040\n보면은 요렇게 있고요이 뭐 보증이\n\n48\n00:01:40,280 --> 00:01:43,200\n보통 간단 사용수 하나 정도는 있는데\n\n49\n00:01:42,040 --> 00:01:45,759\n그냥 박스에 그려져 있는 그게\n\n50\n00:01:43,200 --> 00:01:47,840\n전부인가 봅니다 해서 요것이 본체\n\n51\n00:01:45,759 --> 00:01:49,240\n본체 끝 뭐 교체 가능한 팁 그런 거\n\n52\n00:01:47,840 --> 00:01:51,399\n없어요 그런 건 돈 주고 사시면\n\n53\n00:01:49,240 --> 00:01:52,799\n됩니다 나중에 여기 포장지가 또 친환\n\n54\n00:01:51,399 --> 00:01:54,119\n경기 때문에 종이도 있고요 아\n\n55\n00:01:52,799 --> 00:01:56,560\n농담하는게 아니고 이런 것들이\n\n56\n00:01:54,119 --> 00:01:58,520\n예전에는 다 그런 비닐 플라스틱 같은\n\n57\n00:01:56,560 --> 00:02:02,119\n애들이었는데 요즘은 다 종이로 들어가\n\n58\n00:01:58,520 --> 00:02:04,000\n있어요 사실 친환경 하려면 이런 이런\n\n59\n00:02:02,119 --> 00:02:05,719\n제품을 안 만드는게 친환경이 아닐\n\n60\n00:02:04,000 --> 00:02:07,439\n요쪽에 본체가 있고요 본체가 있고\n\n61\n00:02:05,719 --> 00:02:09,200\n애플 펜슬이라 써 있고 뭐 전반적으로\n\n62\n00:02:07,439 --> 00:02:11,200\n크게 다른 거 같지는 않은데 여기\n\n63\n00:02:09,200 --> 00:02:14,040\n틈바구니 보이죠 여기 틈바구니 있기\n\n64\n00:02:11,200 --> 00:02:16,760\n때문에 쏙 당기면 아 그래도 요거\n\n65\n00:02:14,040 --> 00:02:18,959\n자석으로 반자동이기는네 봐봐 어\n\n66\n00:02:16,760 --> 00:02:21,040\n굉장히 부드럽고 고급스럽게 움직이고요\n\n67\n00:02:18,959 --> 00:02:23,560\n안쪽에 충전 포트가 유광인 데다\n\n68\n00:02:21,040 --> 00:02:26,040\n굉장히 매끈하게 마감이 돼 있고 유광\n\n69\n00:02:23,560 --> 00:02:27,640\n처리를 굉장히 잘했네요이 디테일이\n\n70\n00:02:26,040 --> 00:02:29,360\n포트 디테일 같은 것도 아주 좋긴\n\n71\n00:02:27,640 --> 00:02:31,440\n하다 아 참고로 이건 다들 아시겠지만\n\n72\n00:02:29,360 --> 00:02:33,480\nf 만든 건 아니고요 기존에도 요렇게\n\n73\n00:02:31,440 --> 00:02:34,879\n되는 제품들은 많이 있었습니다 그냥\n\n74\n00:02:33,480 --> 00:02:37,120\n부드럽게 잘 만들었다는 것뿐이에요\n\n75\n00:02:34,879 --> 00:02:38,400\n넘어가면 안 됩니다 왜냐이 친구의\n\n76\n00:02:37,120 --> 00:02:40,200\n가격이 무려 11만 9,000\n\n77\n00:02:38,400 --> 00:02:41,560\n원이에요 교육 할인을 받아도 10만\n\n78\n00:02:40,200 --> 00:02:42,360\n4,000원짜리 11만\n\n79\n00:02:41,560 --> 00:02:44,480\n99,000원에 10만\n\n80\n00:02:42,360 --> 00:02:46,319\n4000원이라는 그냥 비싼 팬이구나\n\n81\n00:02:44,480 --> 00:02:48,159\n하고 감이 안 올 수 있는데 잘 봐요\n\n82\n00:02:46,319 --> 00:02:51,080\n애플 펜슬 1세대 14만 9,000\n\n83\n00:02:48,159 --> 00:02:53,239\n원이고요요 짜플 펜슬 다양한 제품들이\n\n84\n00:02:51,080 --> 00:02:55,360\n있지만 옆에 붙고 무선 충전되는 것\n\n85\n00:02:53,239 --> 00:02:56,560\n중에서 이제 구매하기 제일 쉬운 큐팩\n\n86\n00:02:55,360 --> 00:02:58,319\nES 제일 많이 팔린 걸로 사와\n\n87\n00:02:56,560 --> 00:03:00,200\n봤는데 제품에 따라 달하지만 뭐 2만\n\n88\n00:02:58,319 --> 00:03:02,239\n원에서 뭐 비싼 거는 3만 만원 3만\n\n89\n00:03:00,200 --> 00:03:04,040\n5,000원 정도까지 하죠 그 2세대\n\n90\n00:03:02,239 --> 00:03:05,239\n진짜 애플펜슬 처음에 15만 원\n\n91\n00:03:04,040 --> 00:03:06,319\n하다가 16만 원 하다가 갑자기\n\n92\n00:03:05,239 --> 00:03:07,560\n20만 원 이래가지고 19만\n\n93\n00:03:06,319 --> 00:03:10,280\n5,000원에 내 버렸는데 그거에\n\n94\n00:03:07,560 --> 00:03:12,000\n비해서 11만 9천원이라는 상대적으로\n\n95\n00:03:10,280 --> 00:03:13,879\n저렴해 가지고 가성비 템이라고\n\n96\n00:03:12,000 --> 00:03:16,080\n생각하실 수 있는데 그래서 애플이\n\n97\n00:03:13,879 --> 00:03:18,120\n정신차리라고 여기다가 비교 페이지를\n\n98\n00:03:16,080 --> 00:03:19,920\n만들어 놨습니다 자 2세대에 비해서\n\n99\n00:03:18,120 --> 00:03:22,120\n빠지는 기능들이 있는 거는 납득이\n\n100\n00:03:19,920 --> 00:03:24,239\n되죠 1세대에 비해서도 이거 체크\n\n101\n00:03:22,120 --> 00:03:25,799\n표시돼 있는 거보다 없는 거에 새로\n\n102\n00:03:24,239 --> 00:03:27,720\n지원되는 기능이 더 많으니까 좋아\n\n103\n00:03:25,799 --> 00:03:29,159\n보이네 그럼 가성비가 있나 보다라고\n\n104\n00:03:27,720 --> 00:03:30,799\n생각할 수 있지만 애플이 굉장히\n\n105\n00:03:29,159 --> 00:03:32,640\n자연스럽게 별거 아닌 것처럼 해하는데\n\n106\n00:03:30,799 --> 00:03:34,599\n이게 뭐야 압력 감지가 빠져 있어\n\n107\n00:03:32,640 --> 00:03:36,480\n톡톡해 가지고 도구 바꾸는 거라든지\n\n108\n00:03:34,599 --> 00:03:38,560\n무료 각인 이런 건 가성비가 그럴 수\n\n109\n00:03:36,480 --> 00:03:40,200\n있어 근데 압력 감지가 안 된다는\n\n110\n00:03:38,560 --> 00:03:41,920\n거는 요걸 그림 그리는데 쓰기\n\n111\n00:03:40,200 --> 00:03:43,640\n곤란하다는 거예요 그렇게 봤을 때\n\n112\n00:03:41,920 --> 00:03:45,680\n자플 펜슬이 옆에도 붙고 무선\n\n113\n00:03:43,640 --> 00:03:47,560\n충전까지 지원하는이 시점에 아쉬운\n\n114\n00:03:45,680 --> 00:03:49,400\n점은 압력 감지가 안 된다는 거 밖에\n\n115\n00:03:47,560 --> 00:03:51,640\n없는데 그럼 똑같은 단점을 가진\n\n116\n00:03:49,400 --> 00:03:53,040\n제품을 세 배네 배 심하면 다섯 배\n\n117\n00:03:51,640 --> 00:03:55,400\n주고 사야 되는 물건이란 얘기예요\n\n118\n00:03:53,040 --> 00:03:57,239\n당연히 할 말이 없지는 않아서 호버\n\n119\n00:03:55,400 --> 00:03:58,519\n기능이 됩니다 근데 호버 기능 갤럭시\n\n120\n00:03:57,239 --> 00:04:00,760\n탭 같은 거에서 뭐 당연히 되는\n\n121\n00:03:58,519 --> 00:04:02,879\n기능이지만 아이 패드에서는 11in\n\n122\n00:04:00,760 --> 00:04:04,680\n4세대가 12.9in 6세대에서\n\n123\n00:04:02,879 --> 00:04:06,360\n지원이 되는 기능이에요 근데 그 완전\n\n124\n00:04:04,680 --> 00:04:07,840\n최신 아이패드 프로 사는 사람이 과연\n\n125\n00:04:06,360 --> 00:04:09,920\n7만 6,000원을 아끼자고 이거를\n\n126\n00:04:07,840 --> 00:04:11,480\n살까 생각하면은 저는 요거는 목적이\n\n127\n00:04:09,920 --> 00:04:13,840\n굉장히 확실하다고 생각하는데 그\n\n128\n00:04:11,480 --> 00:04:15,400\n얘기는 제가 써 보면서 차차 말씀을\n\n129\n00:04:13,840 --> 00:04:16,759\n드릴게요 자 최대한의 기능을\n\n130\n00:04:15,400 --> 00:04:18,959\n보여드려야 되니까 그런 이상한\n\n131\n00:04:16,759 --> 00:04:21,560\n사람이라고 생각하고 12,9 6세대\n\n132\n00:04:18,959 --> 00:04:23,360\n붙여 봅시다 옆에 착 달라붙어요 왜\n\n133\n00:04:21,560 --> 00:04:25,240\n안 떠 먹아 아 맞다 이거 붙어가지고\n\n134\n00:04:23,360 --> 00:04:26,479\n페어리가 안 되지 USB 케이블을\n\n135\n00:04:25,240 --> 00:04:28,360\n연결해야 되는 걸 제가 너무나\n\n136\n00:04:26,479 --> 00:04:31,800\n자연스럽게 까먹었는데 옆에 있는\n\n137\n00:04:28,360 --> 00:04:34,880\n케이블을 빼봅시다 옆을 열어 케이블을\n\n138\n00:04:31,800 --> 00:04:36,560\n꽂자 아이패드에 꽂자 야 정말 모양\n\n139\n00:04:34,880 --> 00:04:38,039\n빠진다는 말이 이렇게 잘 어울릴 수가\n\n140\n00:04:36,560 --> 00:04:40,080\n없습니다 와 근데 이거 연결하려고\n\n141\n00:04:38,039 --> 00:04:41,720\n보니까 뭐 케이블을 바꾸고 뭐 별짓을\n\n142\n00:04:40,080 --> 00:04:44,479\n해도 연결이 안 돼 가지고 찾아봤더니\n\n143\n00:04:41,720 --> 00:04:46,080\n꽁꽁 숨겨놓은 지원 페이지에 17.1\n\n144\n00:04:44,479 --> 00:04:47,280\n이상이 필요하다고 써 있어 17.0\n\n145\n00:04:46,080 --> 00:04:49,000\n있데 왜 안 되나 했네 잠시만 나\n\n146\n00:04:47,280 --> 00:04:51,800\n업데이트 좀 할게 오케이 업데이트를\n\n147\n00:04:49,000 --> 00:04:53,680\n마쳤고요 자 한번 꽂아 봅시다 오케이\n\n148\n00:04:51,800 --> 00:04:56,120\n애플 펜슬이라고 떴고 기능상으로 잠깐\n\n149\n00:04:53,680 --> 00:04:58,000\n보면은 배터리 잔량 뜨고요 펜스 호버\n\n150\n00:04:56,120 --> 00:04:59,960\n뜨고요 송글 씨 입력 어쩌고저쩌고\n\n151\n00:04:58,000 --> 00:05:02,000\n요로쿵 저렇쿵 뭐 별다른 차이점 없는\n\n152\n00:04:59,960 --> 00:05:03,759\n것 같이 보이나 애플 펜슬 2랑\n\n153\n00:05:02,000 --> 00:05:05,520\n연결한 화면을 보여 드리면 얘는\n\n154\n00:05:03,759 --> 00:05:07,320\n이중탭이 떠 있는 걸 볼 수 있죠\n\n155\n00:05:05,520 --> 00:05:09,720\n호버 cmr 이중탭 허용이라는 것도\n\n156\n00:05:07,320 --> 00:05:12,520\n차이가 있는 것을 확인할 수 있고요\n\n157\n00:05:09,720 --> 00:05:15,199\n그래서 요렇게 보면은 호버 됩니다\n\n158\n00:05:12,520 --> 00:05:16,520\n신난다 자 제일 중요한 것은 요거는\n\n159\n00:05:15,199 --> 00:05:19,919\n필기 용이라고 말씀을 드렸잖아요\n\n160\n00:05:16,520 --> 00:05:21,759\n그래서 필기를 해 봅시다 필기를 오\n\n161\n00:05:19,919 --> 00:05:23,759\n야 이거 압력 감지가 안 되니까\n\n162\n00:05:21,759 --> 00:05:25,600\n확실히 필기할 때 맛이 좀 떨어지긴\n\n163\n00:05:23,759 --> 00:05:30,000\n한다\n\n164\n00:05:25,600 --> 00:05:32,120\n필기를 할 때 글자라고 치고\n\n165\n00:05:30,000 --> 00:05:38,160\n압력\n\n166\n00:05:32,120 --> 00:05:41,360\n감지가 안 되니 이것 참\n\n167\n00:05:38,160 --> 00:05:42,479\n후저 보이네 압력 감지가 되는 걸로\n\n168\n00:05:41,360 --> 00:05:44,840\n쓰면은\n\n169\n00:05:42,479 --> 00:05:48,000\n필기를 할\n\n170\n00:05:44,840 --> 00:05:50,759\n때 압력 훨씬 더 자연스러운 필기가\n\n171\n00:05:48,000 --> 00:05:53,960\n되는 걸 볼 수 있죠 살짝으면 살짝\n\n172\n00:05:50,759 --> 00:05:55,680\n세게 그으면 세게요 차이 구분이 안\n\n173\n00:05:53,960 --> 00:05:57,680\n된다는 거 당연한 얘기지만 압력\n\n174\n00:05:55,680 --> 00:05:59,840\n감지가 안 된다 뿐이지 뭐 팜리젝션\n\n175\n00:05:57,680 --> 00:06:02,080\n같은 건 됩니다 뭐 나머지는 펜슬\n\n176\n00:05:59,840 --> 00:06:03,360\n2세대의 경우에는요 갈고리 현상이라고\n\n177\n00:06:02,080 --> 00:06:05,919\n부르는 것 때문에 싫어하는 분들이\n\n178\n00:06:03,360 --> 00:06:09,000\n많이 계시는데이 usbc 작동 방식\n\n179\n00:06:05,919 --> 00:06:11,400\n자체는 똑같죠 그래서 똑같이\n\n180\n00:06:09,000 --> 00:06:13,599\n일어납니다 자 그렇다면 자플 펜슬과\n\n181\n00:06:11,400 --> 00:06:15,479\n비교해서 이게 완전히 똑같냐 하면은\n\n182\n00:06:13,599 --> 00:06:17,319\n자플 펜슬도 아주 여러 종류가 있기\n\n183\n00:06:15,479 --> 00:06:19,240\n때문에 제품마다 차이가 있을 수\n\n184\n00:06:17,319 --> 00:06:21,520\n있지만 애플이 제공하는 API 펜슬\n\n185\n00:06:19,240 --> 00:06:23,639\n키트를 그대로 쓴 앱들은 상관이\n\n186\n00:06:21,520 --> 00:06:25,840\n없는데 대표적으로 굿노트처럼\n\n187\n00:06:23,639 --> 00:06:27,440\n자체적으로 펜슬과 통신을 해 가지고\n\n188\n00:06:25,840 --> 00:06:29,800\n필압을 비롯한 알고리즘을 제공하는\n\n189\n00:06:27,440 --> 00:06:31,840\n앱들은 양상으로 당연히 똑같은 야 될\n\n190\n00:06:29,800 --> 00:06:33,840\n거 같은데 공식적으로 애플 펜슬\n\n191\n00:06:31,840 --> 00:06:35,639\n플러스 크레용 man 지원하고\n\n192\n00:06:33,840 --> 00:06:37,599\n서드파티 팬은 지원을 안 한다고\n\n193\n00:06:35,639 --> 00:06:39,720\n명시가 돼 있을 정도거든요 그래서 굿\n\n194\n00:06:37,599 --> 00:06:41,360\n노트에서는 볼펜 같이 필압이 안 되는\n\n195\n00:06:39,720 --> 00:06:43,039\n것들은 상관없습니다 하지만 많이들\n\n196\n00:06:41,360 --> 00:06:45,400\n좋아하시는 만년필 같은 거에서 눈에\n\n197\n00:06:43,039 --> 00:06:48,120\n띄라고 일부러 굵게\n\n198\n00:06:45,400 --> 00:06:49,880\n해놨는데 그냥 애플 펜슬 2세대는\n\n199\n00:06:48,120 --> 00:06:51,759\n요런 식으로 되죠 다른 서드 파티\n\n200\n00:06:49,880 --> 00:06:54,919\n펜으로\n\n201\n00:06:51,759 --> 00:06:57,840\n가면은 이렇게 됩니다 자플 펜슬로\n\n202\n00:06:54,919 --> 00:06:59,560\n가도 마찬가지 그러면 필압 안되는\n\n203\n00:06:57,840 --> 00:07:02,039\n애플 펜슬 괄호열고 usbc 바로\n\n204\n00:06:59,560 --> 00:07:04,879\n다꾸로 가도 똑같을 거\n\n205\n00:07:02,039 --> 00:07:06,520\n같잖아요 다르죠 필압이 되는 거는\n\n206\n00:07:04,879 --> 00:07:08,360\n아닌데 저는 처음에 이거 틸트 때문에\n\n207\n00:07:06,520 --> 00:07:10,120\n그런 줄 알았거든요 틸트 다 되거든요\n\n208\n00:07:08,360 --> 00:07:12,400\n그게 아니더라고요 제가 연구를 해\n\n209\n00:07:10,120 --> 00:07:15,960\n보니까이 속도를 갖다 가져오더라구요\n\n210\n00:07:12,400 --> 00:07:19,160\n그래서 천천히 가면 굵고 빨리 가면은\n\n211\n00:07:15,960 --> 00:07:21,639\n얇아집니다 짜플 펜슬 유해선 안 돼요\n\n212\n00:07:19,160 --> 00:07:23,960\n애플 펜슬 2세대 애플 펜슬 usbc\n\n213\n00:07:21,639 --> 00:07:26,000\n호환되는 펜슬 류 차이가 명확하게\n\n214\n00:07:23,960 --> 00:07:28,599\n보이죠 거기다 확실히 마감이나 특히\n\n215\n00:07:26,000 --> 00:07:30,879\n무게 중심 같은게 꽤 괜찮기는 합니다\n\n216\n00:07:28,599 --> 00:07:33,000\n펜슬 2세대 가 18g 이었죠 펜슬\n\n217\n00:07:30,879 --> 00:07:35,360\n1세대 20g 이고요 자플 펜슬\n\n218\n00:07:33,000 --> 00:07:37,479\n14g이에요 근데이 친구 20g이고\n\n219\n00:07:35,360 --> 00:07:39,160\n무게 중심도 상당히 괜찮은 편입니다\n\n220\n00:07:37,479 --> 00:07:41,440\n무게 중심이 잘못 잡혀 있는 제품\n\n221\n00:07:39,160 --> 00:07:42,919\n같은 경우에는 필기할 때 뭔가\n\n222\n00:07:41,440 --> 00:07:44,440\n이상하다는 느낌이 드는 제품들이\n\n223\n00:07:42,919 --> 00:07:48,879\n있거든요 그리고 당연히 애플\n\n224\n00:07:44,440 --> 00:07:50,840\n제품이니까 펜촉도 2세대와 호환이 어\n\n225\n00:07:48,879 --> 00:07:52,680\n되고요 근데 사실 이건 요즘 나오는\n\n226\n00:07:50,840 --> 00:07:55,319\n자플 펜슬도 펜촉이 상당히\n\n227\n00:07:52,680 --> 00:07:56,960\n괜찮아지기도 했거니와 정품이랑 호환이\n\n228\n00:07:55,319 --> 00:07:58,560\n돼요 그래서 처음 시작할 때도\n\n229\n00:07:56,960 --> 00:08:00,440\n말씀드렸지만 요거는 제가 보기에는\n\n230\n00:07:58,560 --> 00:08:02,759\n굉장히 명확한 하거든요 2세대를\n\n231\n00:08:00,440 --> 00:08:04,960\n저렴하게 대체하는 가성비 제품이\n\n232\n00:08:02,759 --> 00:08:07,360\n아니에요 1세대를 대체하는 제품이라고\n\n233\n00:08:04,960 --> 00:08:08,960\n봐야 되는데 그렇게 생각을 하더라도\n\n234\n00:08:07,360 --> 00:08:10,960\n필압 감지가 안 되는게 결정적이다\n\n235\n00:08:08,960 --> 00:08:12,840\n싶죠 그래서 여기서 나오는 힌트는\n\n236\n00:08:10,960 --> 00:08:14,960\n지금 시점에서 애플 펜슬 1세대를\n\n237\n00:08:12,840 --> 00:08:16,840\n누가 쓰느냐에 아이패드 10세대의\n\n238\n00:08:14,960 --> 00:08:18,360\n황당하게 연결해서 쓰는 경우가 거의\n\n239\n00:08:16,840 --> 00:08:20,360\n전부라고 봐야 될 거예요 그래서\n\n240\n00:08:18,360 --> 00:08:22,840\n아패드 세대처럼 교육용으로 들어가야\n\n241\n00:08:20,360 --> 00:08:24,560\n되는데 빼서 부채처럼 끼우거나 어댑터\n\n242\n00:08:22,840 --> 00:08:26,720\n끼워 가지고 너저분하게 연결하는\n\n243\n00:08:24,560 --> 00:08:28,400\n것보다는 조금 더 점잖게 쓸 수 있는\n\n244\n00:08:26,720 --> 00:08:30,440\n제품을 만들었다라는 보는게 맞을\n\n245\n00:08:28,400 --> 00:08:31,879\n겁니다 이게 USB C 충전되는 거는\n\n246\n00:08:30,440 --> 00:08:33,599\n이게 좋아서가 아니라 아패드\n\n247\n00:08:31,879 --> 00:08:35,360\n10세대요 무선 충전이 안 되기\n\n248\n00:08:33,599 --> 00:08:37,839\n때문이거든 그렇기 때문에 기존에\n\n249\n00:08:35,360 --> 00:08:39,959\n교육용으로 많이 쓰던 로지텍 크레용과\n\n250\n00:08:37,839 --> 00:08:41,479\n거의 동일한 사양을 유지한 거죠 참\n\n251\n00:08:39,959 --> 00:08:43,279\n저렴한 제품도 아닌데 그거 하나 빼\n\n252\n00:08:41,479 --> 00:08:45,480\n가지고 여러 사람 귀찮게 만든다 그죠\n\n253\n00:08:43,279 --> 00:08:47,600\n못 만든 제품이냐 그렇지는 않아요\n\n254\n00:08:45,480 --> 00:08:48,920\n마감 좋고요 무게 균형 좋고요 자석\n\n255\n00:08:47,600 --> 00:08:50,760\n돼 있어 가지고 반자동으로 <\n\n256\n00:08:48,920 --> 00:08:52,920\nbehun 하는 메커니즘이라는 잘\n\n257\n00:08:50,760 --> 00:08:54,320\n맞든 제품이에요 문제는 가격이라는\n\n258\n00:08:52,920 --> 00:08:55,880\n거예요 이게 한 45,000원 5만\n\n259\n00:08:54,320 --> 00:08:57,959\n원쯤 했으면 잡다한 걸 포기하고\n\n260\n00:08:55,880 --> 00:08:59,160\n서라도 짜플 펜슬에 좀 더 부해서 좀\n\n261\n00:08:57,959 --> 00:09:00,640\n더 붙 해게 아니라 두 백이 한데요\n\n262\n00:08:59,160 --> 00:09:02,399\n어떤 자플 펜슬 두 배 가격으로 살\n\n263\n00:09:00,640 --> 00:09:03,959\n가능성이 있다고 생각했겠지만 10만\n\n264\n00:09:02,399 --> 00:09:05,560\n9천원이 나는 순간 일반 소비자\n\n265\n00:09:03,959 --> 00:09:07,079\n용으로는 존재 가치가 없다고 봐야\n\n266\n00:09:05,560 --> 00:09:08,839\n되겠죠 그래서 제가 보기에는 최근\n\n267\n00:09:07,079 --> 00:09:11,160\n막나가는 애플에 막나가는 제품 중에\n\n268\n00:09:08,839 --> 00:09:12,800\n하나인 거 같은데 교육용으로 파니까\n\n269\n00:09:11,160 --> 00:09:14,399\n우리는 신경 쓸 필요가 없다라고\n\n270\n00:09:12,800 --> 00:09:16,279\n하기에는 그럴 거면 일반용으로 팔지\n\n271\n00:09:14,399 --> 00:09:18,279\n말아야죠 일반 소비자용으로 팔고\n\n272\n00:09:16,279 --> 00:09:19,760\n홍보하고 보도자료내는 순간 우리는\n\n273\n00:09:18,279 --> 00:09:21,440\n일반 소비자 입장에서 이걸 판단할\n\n274\n00:09:19,760 --> 00:09:22,959\n수밖에 없어요 자 그래서 어떤 댓글\n\n275\n00:09:21,440 --> 00:09:25,040\n달릴지 뻔히 보이는데 뭐 두목님\n\n276\n00:09:22,959 --> 00:09:27,120\n오늘도 후구 뭐 논리 있지 근데 제가\n\n277\n00:09:25,040 --> 00:09:29,279\n희생에서 써 봤습니다 별로 짝퉁을\n\n278\n00:09:27,120 --> 00:09:30,640\n옹호하고 싶지 않은데요이 뭐 적당 껏\n\n279\n00:09:29,279 --> 00:09:32,839\n애플 편을 들어 주죠 그렇습니다\n\n280\n00:09:30,640 --> 00:09:35,079\n여기까지 애플 펜슬 괄호열고 usbc\n\n281\n00:09:32,839 --> 00:09:36,519\n괄호닫고 였고요 아패드 10세대 함께\n\n282\n00:09:35,079 --> 00:09:37,880\n대량 납품되는게 아니라면 일반\n\n283\n00:09:36,519 --> 00:09:39,880\n소비자는 요걸 찾아볼 필요도\n\n284\n00:09:37,880 --> 00:09:41,600\n없겠습니다 혹시 궁한 점 있으시면\n\n285\n00:09:39,880 --> 00:09:42,920\n댓글 남겨주시면 나 이거 어떠 쓰냐\n\n286\n00:09:41,600 --> 00:09:44,680\n나 이거 돈 주고 샀는데 나는 애플\n\n287\n00:09:42,920 --> 00:09:46,000\n펜스 이미 한자루가 있거든 필압도 안\n\n288\n00:09:44,680 --> 00:09:47,880\n되는 거 어땠을지는 제가 차차\n\n289\n00:09:46,000 --> 00:09:49,720\n생각하면서 울고 있겠습니다 혹시\n\n290\n00:09:47,880 --> 00:09:51,320\n궁금해 있으시면 댓글 남겨주시고 제\n\n291\n00:09:49,720 --> 00:09:55,279\n일 페이스북 네이버 TV 어느면에서도\n\n292\n00:09:51,320 --> 00:09:55,279\n만나는 거 잊지 마세요 다 뵐게요\n\n293\n00:09:58,120 --> 00:10:01,120\n끝\n\n294\n00:10:12,839 --> 00:10:15,839\nr'
    return dummy 

def get_test_dummy():
    return
def get_dummy():
    data={}
    data["middleware"]={}
    data["middleware"]["youtube"]=get_youtube_data_dummy()
    data["middleware"]["review"]=get_review_data_real_dummy()
    data["middleware"]["specification"]=get_specification_data_dummy()
    return data
    
