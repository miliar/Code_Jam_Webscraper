#include <bits/stdc++.h>
using namespace std;

typedef long long int LL;

map<LL,LL> mp;

inline LL maxi(LL a ,LL b){
    return (a)>(b) ? (a):(b);
}

inline LL mini(LL a ,LL b){
    return (a)<(b) ? (a):(b);
}

int main(){

    freopen("C-small-2-attempt1.in","r",stdin);
    freopen("o3smallUpdated.txt","w",stdout);

    int t;
    scanf("%d",&t);
    //cout<<t<<endl;
    for(int g=1;g<=t;g++){

        mp.clear();

        LL n,k;
        scanf("%lld %lld",&n,&k);

        LL iniLen = n;
        LL iniCnt = 1;

        mp[iniLen] = iniCnt;

        printf("Case #");
        printf("%d: ",g);
        map<LL,LL> :: reverse_iterator it;

        for(LL i=0; ;){

                //cout<<i<<endl;
                it = mp.rbegin();
                LL len = it->first;
                LL cnt = it->second;

            if( (i+cnt) >= k ){

                LL finalLen;

                if(len&1){
                    finalLen = floor(len/2LL);
                    printf("%lld %lld\n",finalLen,finalLen);
                }
                else{
                    LL finalLen1 = (len-1)/2LL;
                    LL finalLen2 = len/2;
                    printf( "%lld %lld\n", maxi(finalLen1,finalLen2),mini(finalLen1,finalLen2) );

                }
                   break;
            }else{

                i+=cnt;

                if(len&1){
                    LL newLen = floor(len/2LL);
                    if(newLen > 0) {
                        if( mp.find(newLen)!= mp.end()){
                            LL currCnt = mp[newLen];
                            currCnt += 2*cnt;
                            mp[newLen] = currCnt;
                        }else{
                            mp[newLen] = 2*cnt;
                        }
                    }


                }else{

                    LL newLen1 = (len-1)/2LL;
                    LL newLen2 = len/2;
                    if(newLen1 > 0){
                        if( mp.find(newLen1)!= mp.end()){
                        LL currCnt = mp[newLen1];
                        currCnt += cnt;
                        mp[newLen1] = currCnt;
                        }else{
                            mp[newLen1] = cnt;
                        }
                    }
                    if(newLen2 > 0 ){
                        if(mp.find(newLen2)!= mp.end()){
                            LL currCnt = mp[newLen2];
                            currCnt += cnt;
                            mp[newLen2] = currCnt;
                        }else{
                            mp[newLen2] = cnt;
                        }
                    }

                }
                mp.erase(mp.find(len));

            }
        }
    }

    return 0;
}
