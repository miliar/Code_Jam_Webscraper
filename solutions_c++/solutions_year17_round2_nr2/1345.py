#include<iostream>
#include<string>
#include<vector>
#include<tuple>
#include<utility>
#include<algorithm>
#include<cstdint>

using namespace std;
typedef int64_t var;
var t, n;
vector<tuple<var,var,char,char>> in(3);

//I apologize for this spaghetti, and everything i've ever done

int main(){
    cin >> t;
    for(var _t = 0; _t < t; ++_t){
        string retS;
        cin >> n >> get<0>(in[0]) >> get<1>(in[2]) >> get<0>(in[1]) >> get<1>(in[0]) >> get<0>(in[2]) >> get<1>(in[1]);
        get<2>(in[0])='R';get<3>(in[0])='G';
        get<2>(in[1])='Y';get<3>(in[1])='V';
        get<2>(in[2])='B';get<3>(in[2])='O';
        sort(in.begin(),in.end(),greater<tuple<var,var,char,char>>());
        if(get<0>(in[0])>n/2){
            goto fail;
        }
        if(get<0>(in[0])==n/2&&get<1>(in[0])==n/2){
            for(var i = 0; i < get<0>(in[0]); ++i){
                retS.push_back(get<2>(in[0]));
                retS.push_back(get<3>(in[0]));
            }
            goto print;
        }
        for(auto & it: in){
            get<0>(it)-=get<1>(it);
            if(get<1>(it)&&get<0>(it)<1){
                goto fail;
            }
        }
        {
            string suffix;
            while(suffix.length()+retS.length()!=n){
                sort(in.begin(),in.end(),greater<tuple<var,var,char,char>>());
                var i = 0;
                if(retS.length()&&retS.back()==get<2>(in[i])){
                    i = 1;
                    if(!get<0>(in[i])){
                        goto fail;
                    }
                }
                if((!suffix.size())&&retS.length()&&get<0>(in[i])==1&&retS[0]!=get<2>(in[i])){
                    suffix.push_back(get<2>(in[i]));
                    --get<0>(in[i]);
                    while(get<1>(in[i])){
                        suffix.push_back(get<3>(in[i]));
                        suffix.push_back(get<2>(in[i]));
                        --get<1>(in[i]);
                    }
                }else{
                    retS.push_back(get<2>(in[i]));
                    --get<0>(in[i]);
                    while(get<1>(in[i])){
                        retS.push_back(get<3>(in[i]));
                        retS.push_back(get<2>(in[i]));
                        --get<1>(in[i]);
                    }
                }
            }
            retS.append(suffix);
        }
print:
        cout << "Case #" << (_t+1) << ": " << retS << endl;
        continue;
fail:
        cout << "Case #" << (_t+1) << ": IMPOSSIBLE" << endl;
    }
    return 0;
}
