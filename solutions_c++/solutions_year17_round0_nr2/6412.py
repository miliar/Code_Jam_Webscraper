#include<bits/stdc++.h>
using namespace std;

string chh;

int main(void){
    int testCases;
    cin>>testCases;
    for(int testCase=1;testCase<=testCases;testCase++){
        cin>>chh;
        int refs=0;
        while(!refs){
            int len=chh.size();
            for(int i=0;i<len-1;i++)
                if(chh[i]>chh[i+1]){
                    chh[i]=chh[i]-1;
                    for(int j=i+1;j<len;j++)
                        chh[j]='9';
                }
            int t1s=0;
            for(int i=0;i<len-1;i++)
                if(chh[i]>chh[i+1]){
                    t1s=1;
                    break;
                }
            if(t1s==0)
                refs=1;
        }
        cout<<"Case #"<<testCase <<": ";
        int len=chh.size(),j;
        for(int i=0;i<len;i++)
            if(chh[i]!='0'){
                j=i;break;
            }
        for(int i=j;i<len;i++)
            cout<<chh[i];
        cout<<endl;
    }
    return 0;
}
