# Pdisk Api
Pdisk.me webscraper using python fastapi to get the download url, name, created date and time

### Api Usage

#### Fetch the data

```

http://pdisk.api.devlion.tech/get?url={pdisk-link}

```

#### Example

```

http://pdisk.api.devlion.tech/get?url=https://pdisk.pro/j1ul25fk4gbq

```

#### Response

```

{

   "title":"Baywatch_2017_720p_Blu_Ray_DD5_1_192Kbps_Tel__2B_T…",

   "size":1405685453,

   "link":"https://fs3.pdisk.pro:183/d/iy7rcsgcmezfofqkciawx5dnx2mdv5jsjvmnzag2d6wvv7u2fll5azixukpsps67i23tlj25/video.mkv.mp4",

   "created_time":"2023-04-29 11:22:36"

}

```

