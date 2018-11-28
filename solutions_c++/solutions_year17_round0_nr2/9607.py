#include<bits/stdc++.h>
using namespace std;
/*void recall(char *s) {
int i,j,l;
l=strlen(s)-1;
//cout<<l<<endl;
	while(*(s+j)>*(s+j-1)&&j>=0) {j--; }
//	cout<<s<<endl;
	while(*(s+j)==48&&j>=0) {j--;}
//	cout<<s<<endl;
	if(*(s+j)==49) {
	s[j]=='\t';
	for(i=j+2;i<=l;i++) *(s+i)==57;
	}
	else {
	    int k=*(s+j+1);
	    *(s+j+1)=k-1;
	for(i=j+2;i<=l;i++) *(s+i)=57;
	}
//	cout<<s<<endl;
}*/
int main()
{

int t,i,j,l;
char s[20];
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>s;
		l=strlen(s)-1;
		for(j=0;j<l;j++) {
		    if(s[l-j]<s[l-j-1]) {
		        s[l-j-1]-=1;
		        for(int k=l-j;k<=l;k++) s[k]=57;
		    }
		}

		cout<<"Case #"<<i+1<<": ";
		j=0;
		while(s[j]==48) j++;
		for(int k=j;k<l+1;k++) cout<<s[k];
		cout<<endl;

	}
}
