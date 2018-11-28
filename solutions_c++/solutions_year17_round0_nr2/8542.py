#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int main()
{
	int T;
	cin>>T;
	unsigned long long int N;
	for(int i=1;i<=T;i++)
	{		
		cin>>N;
		
			string num = to_string(N);
			if(is_sorted(num.begin(), num.end()))
			{
				cout<<"Case #"<<i<<": "<<num<<"\n";
				
			}
			else
			{
				if(count(num.begin(),num.end()-1,'1')==num.length()-1)
				{
					auto e = is_sorted_until(num.begin(),num.end());
					fill(e,num.end(),'9');					
					num[0] = '0';
					for_each(num.begin()+1,e,[](auto &ch)
					{
						ch='9';
					});
					N = stoll(num);
					cout<<"Case #"<<i<<": "<<N<<"\n";				
					//break;
				}
				else
				{
					auto e = is_sorted_until(num.begin(),num.end());
					fill(e,num.end(),'9');					
					char prev_old = *(e-1);
					*(e-1) = (char)(((int)(*(e-1)-'0') - 1)+'0');
					char prev_new = *(e-1);
					bool flag = 0;
					for_each(num.begin(),e-1,[prev_old,prev_new,&flag](auto &ch)
					{
						if(ch==prev_old && flag == 1)
							ch = '9';
						if(ch==prev_old && flag == 0)
						{
							flag = 1;
							ch = (char)(((int)(ch -'0') - 1)+'0');
						}
					});
					if(flag==1)
						*(e-1)='9';
					cout<<"Case #"<<i<<": "<<stoll(num)<<"\n";				
					//break;
					
				}
			}
		//}		
	}
}
