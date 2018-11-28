#include <bits/stdc++.h>
#define MAX 1100

using namespace std;

int main()
{
    //freopen("input.txt","r", stdin);
    //freopen("output.txt","w", stdout);
	int t;
	cin>>t;
	for(int cas=1;cas<=t;cas++){
		string s;
		cin>>s;
		int i;
		int f=0;
		for( i = 0; i<s.length()-1; i++){
           if(s[i+1]-s[i]<0){
            f=1;
            break;
            }
        }
        if(f){
            for(int j=i+1; j<s.length();j++)
                s[j]='9';
            //cout<<"Value of I "<<i<<endl;
            s[i]=(char)(s[i]-1);
           // for(int l=0;l<s.length();l++)
          //      cout<<s[l];
          //  cout<<endl;
            while(i>0 && s[i]<s[i-1]){
                s[i]='9';
                s[i-1]--;
                i--;
                }
            }
            i=0;
            while(s[i]=='0')
                i++;
        cout<<"Case #"<<cas<<':'<<' ';
        for(;i<s.length();i++)
            cout<<s[i];
        cout<<endl;
	}
    return 0;
}
