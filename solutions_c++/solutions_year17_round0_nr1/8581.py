#include<iostream>
#include<fstream>
using namespace std;
int main(){
    int T=0,K=0;
    string S;
    ifstream iF ("A-large (1).in");
    ofstream oF ("output.txt");
    iF>>T;
    for(int i=0;i<T;i++)
        {
        int j=0, ctr=0, ans=0;
        iF>>S>>K;
        while(K<=(S.length()-j)){
            if(S[j]=='-'){
                int b=j;
                for(int l=0;l<K;l++){
                    if(S[b]=='-')
                        S[b]='+';
                    else
                        S[b]='-';
                    b++;
                    if(l==0)
                        ctr++;
                }
            }
            j++;
        }
        for(int a=0;a<S.size();a++){
            if(S[a]=='+')
                ans++;
        }
        oF<<"Case #"<<i+1<<": ";
        if(ans==S.size())
            oF<<ctr;
        else
            oF<<"IMPOSSIBLE";
        oF<<endl;
    }
    iF.close();
    oF.close();
    return 0;
}
