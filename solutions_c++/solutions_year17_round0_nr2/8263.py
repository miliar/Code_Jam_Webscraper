#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>

using namespace std;
int T;
char n[20];
string num;

long long getpre(){
    strcpy(n,num.c_str());
    int len = strlen(n);
    int i=0,j=0;
    for(i=0;i<len-1;i++){
        if(n[i]>n[i+1])
            break;
    }
    if(i!=len-1){
        j = i;
        while(n[j]==n[i])   j--;
        i = j+1;
        n[i] -= 1;
    }
    for(j=i+1;j<len;j++)
        n[j] = '0' + 9;
    
    int t =0;
    long long result = 0;
    while(!n[t]) t++;
    for(i=t;i<len;i++){
        result *= 10;
        result += n[i]-'0';
    }
    return result;
}

int main()
{
	freopen("in","r",stdin);
	freopen("result","w",stdout);
    cin>>T;
    for(int i=1;i<=T;i++){
        cin>>num;
        cout<<"Case #"<<i<<":"<<" "<<getpre()<<endl;
    }
}
