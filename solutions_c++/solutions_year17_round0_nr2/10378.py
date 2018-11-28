#include<iostream>
using namespace std;

int main()
{
	int c,i;
	long int tmp,t,last,digit;
	cin>>c;
	long int num[c];
	for(i=0; i<c; i++)
	{
		cin>>num[i];
	}
	
	for(i=0; i<c; i++)
	{
		cout<<"case #"<<i+1<<": ";
		tmp = num[i];
		//cout<<tmp<<"\t";
		while(tmp > 0)
		{
			t = tmp;
				last = t % 10;
				t=t/10;
				while(t>0){				
					digit = t % 10;
					if(!(last >= digit))
						goto next;
					t /= 10;
					last = digit;
				}
				cout<<tmp;
				break;
		next:	
			tmp=tmp-1;		
		}
		
		cout<<endl;
	}
	
	
	return 0;

}
