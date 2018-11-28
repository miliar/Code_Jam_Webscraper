#include<iostream>
#include<vector>
#include<cstdio>
#include<string>

using namespace std;

main()
{
    freopen("input.txt","r",stdin);
    freopen("smallBout.txt","w",stdout);
    int T,counter=1;//,K;

    bool done;
    //long long N;

    cin>>T;
    while(counter<=T){
        //cin>>S>>K;
        string S;
        cin>>S;

        unsigned long long N = stoull(S);

        for(int j=N;j>0;j++){
            int len= S.length();
            --len;
            if(len==0){
            cout<<"Case #"<<counter<<": "<<N;break;}
            for(int i=0;i<len;i++){
                int tmp1 = S[i]-48;
                int tmp2 = S[i+1]-48;
                if(tmp1-tmp2>0){
                    done = false;
                    break;
                }
                else done = true;
            }
            if(done){
                cout<<"\nCase #"<<counter<<": "<<N;
                break;
            }
            N--;
            S=to_string(N);
        }
        counter++;
    }
}
