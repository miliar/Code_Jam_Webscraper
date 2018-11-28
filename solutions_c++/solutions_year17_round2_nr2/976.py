#include<bits/stdc++.h>
using namespace std;
#define redirect_in
#define redirect_out
#define debug
string IC="ROYGBV";
vector<int> unicores;
vector<string> extra;

void print(int & cas){
    cout<<"Case #"<<++cas<<": IMPOSSIBLE"<<endl;
}

void print(int & cas, string ans){
    cout<<"Case #"<<++cas<<": "<<ans<<endl;
}

int main(){
#ifdef redirect_in
    freopen("b.in", "r", stdin);
#endif
#ifdef redirect_out
    freopen("b.out", "w", stdout);
#endif
    int T, N, cas=0;
    cin>>T;
    while(T--){
        unicores.clear(); unicores.resize(6);
        int sum=0;
        cin>>N;
        for(int i=0; i<6; ++i){
            cin>>unicores[i];
            sum+=unicores[i];
        }
        if(sum!=N){
            print(cas);
            continue;
        }
        string ans;

        extra.clear(); extra.resize(6);
        if(unicores[1]>0){
            if(unicores[1]+unicores[4]==N){
                if(unicores[1]!=unicores[4]){
                    print(cas);
                    continue;
                }else{
                    string ans;
                    for(int i=0; i<unicores[1]; ++i){
                        ans+=IC[1];
                        ans+=IC[4];
                    }
                    print(cas, ans);
                    continue;
                }
            }
            if(unicores[4]<unicores[1]+1){
                print(cas);
                continue;
            }else{
                unicores[4]=unicores[4]-unicores[1];
                for(int i=0; i<unicores[1]; ++i){
                    extra[4]+=IC[4];
                    extra[4]+=IC[1];
                }
                extra[4]+=IC[4];
                N-=2*unicores[1];
                unicores[1]=0;
            }
        }

       if(unicores[3]>0){
            if(unicores[3]+unicores[0]==N){
                if(unicores[3]!=unicores[0]){
                    print(cas);
                    continue;
                }else{
                    string ans;
                    for(int i=0; i<unicores[3]; ++i){
                        ans+=IC[3];
                        ans+=IC[0];
                    }
                    print(cas, ans);
                    continue;
                }
            }
            if(unicores[0]<unicores[3]+1){
                print(cas);
                continue;
            }else{
                unicores[0]=unicores[0]-unicores[3];
                for(int i=0; i<unicores[3]; ++i){
                    extra[0]+=IC[0];
                    extra[0]+=IC[3];
                }
                extra[0]+=IC[0];
                N-=2*unicores[3];
                unicores[3]=0;
            }
        }

        if(unicores[5]>0){
            if(unicores[5]+unicores[2]==N){
                if(unicores[5]!=unicores[2]){
                    print(cas);
                    continue;
                }else{
                    string ans;
                    for(int i=0; i<unicores[5]; ++i){
                        ans+=IC[5];
                        ans+=IC[2];
                    }
                    print(cas, ans);
                    continue;
                }
            }
            if(unicores[2]<unicores[5]+1){
                print(cas);
                continue;
            }else{
                unicores[2]=unicores[2]-unicores[5];
                for(int i=0; i<unicores[5]; ++i){
                    extra[2]+=IC[2];
                    extra[2]+=IC[5];
                }
                extra[2]+=IC[2];
                N-=2*unicores[5];
                unicores[5]=0;
            }
        }

        int min_val=1005, min_pos=-1, max_val=0, max_pos=-1, middle_val=0, middle_pos=-1;
            for(int j=0; j<6; j+=2){
                if(unicores[j]==0)
                    continue;
                if(unicores[j]>max_val){
                    max_val=unicores[j];
                    max_pos=j;
                }
                if(unicores[j]<=min_val){
                    min_val=unicores[j];
                    min_pos=j;
                }
            }

        for(int j=0; j<6; j+=2){
            if(unicores[j]==0) continue;
            if(j!=max_pos&&j!=min_pos){
                middle_pos=j;
                middle_val=unicores[j];
            }
        }
        if(min_pos==max_pos){
            print(cas);
            continue;
        }
//        cout<<max_pos<<" "<<max_val<<" "<<middle_pos<<" "<<middle_val<<" "<<min_pos<<" "<<min_val<<endl;
        if(middle_pos==-1){
            if(min_val!=max_val){
                print(cas);
                continue;
            }else{
                string ans;
                for(int i=0; i<N; ++i){
                    if(i%2){
                        if(!extra[min_pos].empty()){
                            ans+=extra[min_pos];
                            extra[min_pos].clear();
                        }else{
                            ans+=IC[min_pos];
                        }
                    }else{
                        if(!extra[max_pos].empty()){
                            ans+=extra[max_pos];
                            extra[max_pos].clear();
                        }else
                            ans+=IC[max_pos];
                    }
                }
                print(cas, ans);
            }
        }else{
            int diff=max_val-middle_val;
            if(min_val<diff||min_val>diff+2*middle_val){
                print(cas);
            }else{
                string ans;
                for(int i=0; i<middle_val; ++i){
                    if(!extra[max_pos].empty()){
                        ans+=extra[max_pos];
                        extra[max_pos].clear();
                    }else
                        ans+=IC[max_pos];
                    if(min_val>diff){
                        --min_val;
                        if(!extra[min_pos].empty()){
                            ans+=extra[min_pos];
                            extra[min_pos].clear();
                        }else
                        ans+=IC[min_pos];
                    }
                    if(!extra[middle_pos].empty()){
                        ans+=extra[middle_pos];
                        extra[middle_pos].clear();
                    }else
                    ans+=IC[middle_pos];
                    if(min_val>diff){
                        --min_val;
                        if(!extra[min_pos].empty()){
                            ans+=extra[min_pos];
                            extra[min_pos].clear();
                        }else
                        ans+=IC[min_pos];
                    }
                }
                max_val-=middle_val;
                while(max_val--){
                    if(!extra[max_pos].empty()){
                        ans+=extra[max_pos];
                        extra[max_pos].clear();
                    }else
                    ans+=IC[max_pos];
                    if(!extra[min_pos].empty()){
                        ans+=extra[min_pos];
                        extra[min_pos].clear();
                    }else
                    ans+=IC[min_pos];
                }
                print(cas, ans);
            }
        }

    }

    return 0;
}

