#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
void first_case(string str){
	ll i;
	for( i=1;i<str.length();i++){
		if(str[i-1]!=str[i])
			break;
	}
	str[i]=str[i]-1;
	i++;
	for(;i<str.length();i++)
		str[i]='9';
	cout<<str;
}
void second_case(string str,ll i){
	if(i==0 && str[i]=='1'){
		for(ll i=0;i<str.length()-1;i++)
			cout<<'9';
	}else{
		//str[i]--;
		for (;i>0 && str[i]==str[i-1];i--);
		str[i]--;
		//cout<<i<<"  "<<str<<endl;
		for(i=i+1;i<str.length();i++)
			str[i]='9';
		cout<<str;
	}
}
int main()
{
	string str,str2;
	ll test,i;
	cin>>test;
	for (ll t = 1; t <= test; ++t)
	{	cin>>str;
		cout<<"Case #"<<t<<": ";
		for ( i = 1; i < str.length(); ++i)
		{
			/*if (str[i-1]<str[i])
			{
				first_case(str);
				break;
			}*/
			if(str[i-1]>str[i]){
				second_case(str,i-1);
				break;
			}
		}
		if(i>=str.length())
			cout<<str;
		cout<<endl;
	}
	return 0;
}