#include<iostream>
using namespace std;
int check(int num)
{
//cout<<num<<" ";
int i = 0; // the array index
int a[1000],b[1000]; // the array
		while (num) { // loop till there's nothing left
		    a[i] = num % 10; // assign the last digit
		    num /= 10; // "right shift" the number
		    //cout<<i<<"="<<a[i]<<" ";
		    i++;
		    
		}

//for(int k=0;k<(i);k++)
//	cout<<a[k]<<" ";		

int j=0,len=i-1;
		while(i--)
		{b[j++]=a[i];}

for(int i=0;i<len;i++)
	{	if(b[i]>b[i+1])
			return 0;
	}
return 1;

}
int main()
{
int i,t,c=1,num;
cin>>t;
	if(t<1||t>100)
	return 0;
while(t--){
cin>>num;
	if(num<1||num>1000)
	return 0;
	
for(i=num;i>0;i--)
	{if(check(i)==1)
		{
		//cout<<"\n"<<i;
		break;
	}
	}

cout<<"case #"<<c<<":"<<" "<<i<< endl;
c++;
}
//cout<<"\n"<<check(c)<<endl;
return 0;
}
