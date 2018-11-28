#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
cin >> t;
string a;
int flag;
for(int i=1;i<=t;i++){
cin >> a;
if(a.size()==1)
{
cout <<"Case #"<<i<<": "<< a << "\n";
}
else
{
for(int j=0;j<a.size()-1;j++)
{
	if(a[j]>a[j+1])	{
		int d = j;
		while(a[d]==a[d-1] && d!=0){
			d--;
		}
		a[d]=a[d]-1;
		for(int e=d+1;e<a.size();e++)
			a[e]='9';
	}
}
int j=0;
for( j=0;j<a.size();j++){
	if(a[j]!='0')
		break;
}
cout <<"Case #"<<i<<": "<< a.substr(j) << "\n";
}
}
}
