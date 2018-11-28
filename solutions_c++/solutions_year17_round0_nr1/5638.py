#include<iostream>
using namespace std;
string swap(string s,int i,int k){
    for(int j=i;j<k+i;j++)
    if(s[j]=='-')
        s[j]='+';
    else
        s[j]='-';
    return s;
}
int main(){
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
    int t;
    cin>>t;
    for( int tc=0;tc<t;tc++){
        string s;
		cin>>s;
    int l = s.length();
        int k,c=0,i;
        cin>>k;
        for( i=0;i<l-k+1;i++){
            if(s[i]=='-'){
             s = swap(s,i,k);
                c++;
            }
        }
        for( i=0;i<l;++i){
            if(s[i]=='-')
                break;
        }
        if(i==l)
            cout<<"Case #"<<tc+1<<": "<<c<<endl;
        else
            cout<<"Case #"<<tc+1<<": IMPOSSIBLE"<<endl;
    }
    fclose(stdout);
    return 0;
}