#include <iostream>
#include <string>
using namespace std;

int process(int block1, int gap, int block2, int k)
{
	int block1_r = block1 %k, block2_r = block2 % k;
	int mod;
	//cout<<"inside process"<<endl;
	//cout<<block1_r<<","<<block2_r<<endl;
	if(block1_r == block2_r)
	{
		mod = k - block1_r;
		//cout<<"same and hence mod is "<<mod<<endl;
	}
	else if(block1_r + block2_r == k)
	{
		mod = 0;
		//cout<<"mod is empty"<<endl;
	}
	else
	{
		return -1;
		//cout<<"return -1"<<endl;
	}
	if(k == 2 && mod == 1)
	{
		return gap + 1;
	}
	else if(mod == 0 && gap % k == 0)
	{
		return (gap/k) * 2 + 1;
	}
	if(gap % k == mod)
	{
		//cout<<gap/k<<endl;
		return (gap/k) * 2 + 2;
	}
	return -1;
}
int main()
{
	int t;
	freopen ("/Users/saravanakumars/Downloads/input.txt","r",stdin);
	freopen ("/Users/saravanakumars/Downloads/output.txt","w",stdout);
	cin>>t;
	for(int i = 1;i <= t;i++)
	{
		string g;
		int k;
		cin>>g>>k;
		bool is_negative_block, was_negative_block;
		int is_negative_count, was_negative_count;
		is_negative_block = was_negative_block = false;
		is_negative_count = was_negative_count = 0;
		int gap = 0, ans = 0;
		if(k == 3)
		{
			size_t nPos = g.find("-+-+-", 0); 
			while(nPos != string::npos)
			{
				g.replace(nPos, 5, "--+--");
				ans++;
				nPos = g.find("hello", nPos+1);
			}
		}
		//cout<<"the replaced string is "<<g<<endl;
		bool impossible = false;
		for(int j = 0; j < g.size();j++)
		{
			//cout<<"char is "<<g[j]<<endl;
			if(g[j] == '-')
			{
				is_negative_block = true;
				is_negative_count++;
				//cout<<"negative count "<<is_negative_count<<endl;
			}
			else
			{
				if(is_negative_block)
				{
					//cout<<"is negative block"<<endl;
					if(!was_negative_block)
					{
						//cout<<"there was a negative block"<<endl;
						if(is_negative_count % k == 0)
						{
							ans += is_negative_count/k;
							//cout<<"not adding the current one as it is a exact multiple"<<ans<<endl;
						}
						else
						{
							ans += is_negative_count/k;
							was_negative_block = true;
							was_negative_count = is_negative_count % k;
							//cout<<"adding the current one as the previous "<<ans<<","<<was_negative_count<<endl;
						}
					}
					else
					{
						//cout<<"now computing its"<<endl;
						ans += is_negative_count/k;
						int count;
						if((count = process(was_negative_count, gap, is_negative_count % k, k)) != -1)
						{
							//cout<<"count is "<<count<<endl;
							ans += count;
						}
						else
						{
							//cout<<"count is -1"<<endl;
							impossible = true;
							break;
						}
						was_negative_count = 0;
						was_negative_block = false;
					}
					is_negative_count = 0;
					is_negative_block = false;
					gap = 0;
				}
				gap++;
				//cout<<"gap is "<<gap<<endl;
			}
		}
		//cout<<"hell outside"<<endl;
		if(was_negative_block && !is_negative_block)
		{
			impossible = true;
		}
		if(is_negative_block)
		{
			is_negative_block = false;
			if(!was_negative_block)
			{
				if(is_negative_count % k == 0)
				{
					ans += is_negative_count/k;
					//cout<<"not adding the current one as it is a exact multiple"<<ans<<endl;
				}
				else
				{
					impossible = true;
				}
			}
			else
			{
				int count;
				ans += is_negative_count/k;
				if((count = process(was_negative_count, gap, is_negative_count % k, k)) != -1)
				{
					//cout<<"count is "<<count<<endl;
					ans += count;
				}
				else
				{
					//cout<<"count is -1"<<endl;
					impossible = true;
				}

			}
		}
		if(impossible)
		{
			cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
		}
		else
		{
			cout<<"Case #"<<i<<": "<<ans<<endl;
		}
	}
}
