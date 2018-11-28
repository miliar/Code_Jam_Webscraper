#include<iostream>
using namespace std;
string flip(string s,int i,int k){
    for(int j=i;j<k+i;j++)
    if(s[j]=='-')
        s[j]='+';
    else
        s[j]='-';
    return s;
}
int main(){
	freopen("input.cpp","r",stdin);
	freopen("output.cpp","w",stdout);
    int T;
    cin>>T;
    for( int t=0;t<T;++t){
        string s;
        cin>>s;
    int n = s.length();
        int k,c=0,i;
        cin>>k;
        for( i=0;i<n-k+1;i++){
            if(s[i]=='-'){
             s = flip(s,i,k);
                c++;
            }
        }
        for( i=0;i<n;++i){
            if(s[i]=='-')
                break;
        }
        if(i==n)
            cout<<"Case #"<<t+1<<": "<<c<<endl;
        else
            cout<<"Case #"<<t+1<<": IMPOSSIBLE"<<endl;
    }
    fclose(stdout);
    return 0;
}
