#include <iostream>

using namespace std;

int main()
{
    int T;
    cin>>T;
    for(int a=1;a<=T;a++){
        std::string S;
        cin>>S;
        int K;
        cin>>K;
        int i=0;
        int count=0;
        int l=S.length();
        //cout<<"l="<<l<<endl;
        while(i<l-K+1){
            if(S[i]=='-'){
                for(int j=i;j<i+K;j++){
                    if(S[j]=='-'){
                        S[j]='+';
                    }else{
                        S[j]='-';
                    }
                }
                count++;
            }

            //cout<<S<<endl;

            i++;
        }
        int flag=0;
        for(int b=0;b<l;b++){
            if(S[b]=='-')
                flag=1;
        }
        if(flag==1)
            cout<<"Case #"<<a<<": IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<a<<": "<<count<<endl;
    }
    return 0;
}
