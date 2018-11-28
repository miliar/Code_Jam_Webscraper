#include<iostream>
#include<cmath>
using namespace std;
int main()
{
	int t,i;
	cin>>t;
	for(i=0;i<t;i++)
	{
		int n,j,numb,rem[20],index=0,r,y,res=0;
		cin>>n;
		for(j=n;j>0;j--)
		{
			numb=j;
			while(numb!=0)
			{
				r=numb%10;
				rem[index]=r;
				index++;
				numb=numb/10;
			}
			for(y=0;y<index-1;y++)
			{
				if(rem[y]<rem[y+1])
					break;
			}
			if(y==(index-1))
			{
				for(int z=0;z<index;z++)
				{
					int adder=1;
					int p=z;
					if(p==0)
                        adder=1;
                    else{
                        while(p!=0)
                        {
                            adder=adder*10;
                            p--;
                        }
                    }
					res=res+(rem[z]*adder);
				}
				break;
			}
			index=0;
		}
		cout<<"Case #"<<i+1<<": "<<res<<endl;

	}
}
