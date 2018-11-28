#include <iostream>
#include <string.h>
using namespace std;
void checkdigits(char* num)
{
int previous,next,length;
length=strlen(num)-1;
previous=length;
next=previous-1;
while(next>=0)
{
if(num[next]>num[previous])
{while(next<previous){
	num[previous]='9';
	previous--;
}
num[next]--;
}
else if(num[next]<num[previous]||num[previous]=='9')
previous--;
next--;
}
for(previous=0;previous<length;previous++){
	if(num[previous]>num[previous+1])
	 num[previous+1]='9';
}
}
int main() {
	int t,i,j,check=0,len,f=0;
	char n[20];
	cin>>t;
	for(i=1;i<=t;i++)
	{f=0;
		cin>>n;
        checkdigits(n);
		cout<<"Case #"<<i<<": ";
		len=strlen(n);
		for(j=0;j<len;j++){
		 if(f==0 && n[j]=='0')
		 {continue;}
		 else{
		 	f=1;
		 	cout<<n[j];
		 }}
		 cout<<endl;
	}
	return 0;
}