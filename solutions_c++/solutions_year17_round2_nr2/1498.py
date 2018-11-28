#include <iostream>
#include <string>
using namespace std;
int main()
{
	int t,n,r,o,y,g,b,v,val,test,grid[3],in1,in2,i;
	char max,chara[3];
	string str;
	cin>>t;
	for(test=1;test<=t;test++)
	{
		str="";
		cin>>n>>r>>o>>y>>g>>b>>v;
		if(r>=y && r>=b){
			max='R';
			in1=1;in2=2;
			val=r;
		}
		else if(y>=r and y>=b){
			max='Y';
			in1=0;in2=1;
			val=y;
		}
		else{
			in1=0;in2=2;
			val=b;
			max='B';
		}
		grid[0]=r;grid[1]=b;grid[2]=y;
		chara[0]='R';chara[1]='B';chara[2]='Y';
		if((n-val)<val)
			cout<<"Case #"<<test<<": IMPOSSIBLE\n";
		else
		{
			for(i=0;i<val-1;i++)
			{
				str+=max;
				if(grid[in1]!=0){
					str+=chara[in1];
					grid[in1]--;
				}
				if(grid[in2]!=0 && grid[in2]>(val-i-1))
				{
					str+=chara[in2];
					grid[in2]--;
				}

			}
			str+=max;
			if(grid[in1])
				str+=chara[in1];
			if(grid[in2])
				str+=chara[in2];
			cout<<"Case #"<<test<<": "<<str<<endl;;
		}

	}
}