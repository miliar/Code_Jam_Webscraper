#include <bits/stdc++.h>
using namespace std;

void overlay(char *num,int index){
    int j = index, i;
    while (j>=0&&num[j]>num[j+1]){
        num[j]--,j--;
    }
    j+=2;
    i = j;
    if (j==1 && num[j-1] == '0')i = j-1;
    while (num[j]!=0)num[i]='9',i++,j++;
    num[i] = 0;
}

int main(){
    char num[20];
    int t,ncase=1,wsize;
    cin>>t;
    while(t>0){
        cin>>num;
        wsize = strlen(num);
        for (int i=1;i<wsize;i++){
            if (num[i]<num[i-1]){
                overlay(num,i-1);
                break;
            }
        }
        cout<<"Case #"<<ncase++<<": "<<num<<endl;
        t--;
    }
}
