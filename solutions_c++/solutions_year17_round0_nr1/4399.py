#include <iostream>
#include <string>

using namespace std;


int main()
{
    long test,caso=1,ans,N;
    cin>>test;
    string P;
    while(caso<=test){
        cin>>P;
        cin>>N;
        ans=0;
        while(P.size()>=N){
            while(P.back()=='+')
                P.pop_back();
            if(P.size()<N)
                break;
            for(int i=0;i<N;++i){
                if(P[P.size()-1-i]=='+')
                    P.replace(P.size()-1-i,1,"-");
                else
                    P.replace(P.size()-1-i,1,"+");
            }
            ans++;
        }
        if(P.size()==0){
            cout<<"Case #"<<caso<<": "<<ans<<endl;
            caso++;
        }
        else{
            cout<<"Case #"<<caso<<": "<<"IMPOSSIBLE"<<endl;
            caso++;
        }
    }
    return 0;
}
