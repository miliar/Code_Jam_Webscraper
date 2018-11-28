#include <bits/stdc++.h>
using namespace std;

int main()
{
	int n,l,k,m[30],a=1,t;
	char s[30];
	cin>>n;
	while(n--){
		cin>>s;
		l=strlen(s);
		k=-1;
		for(int q=0;q<l;++q)m[q]=s[q]-'0';
		for(int q=l-1;q>0;--q){
			if(m[q]<0){
				t=1;
				m[q-1]--;
				k=q-1;
			}
			else if(m[q-1]>m[q]){
				k=q-1;
				m[q-1]--;
			}
		}
		cout<<"Case #"<<a++<<": ";
		for(int q=0;q<k;++q)cout<<m[q];
		if(k==-1)
			cout<<s<<endl;
		else{
			if(!(k==0&&m[0]==0))cout<<s[k]-'0'-1;
			for(int q=k+1;q<l;++q)cout<<'9';
			cout<<endl;
		}
	}
	return 0;
}

