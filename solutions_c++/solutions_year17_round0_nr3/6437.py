#include<fstream>
using namespace std;
int main()
{
	ifstream cin("C-small-1-attempt0.in");
	ofstream cout("out");
	int num;
	cin>>num;
	for(int a=1;a<=num;a++)
	{
		long long  n,ppl;
		cin>>n>>ppl;
		bool arr[n+2]={};
		arr[0]=arr[n+1]=1;
		long long  smallest=-1;
		long long  temp,largest=0;
		long long left,right;
		long long ansmin,ansmax;
		long long pos;
		for(int i=0;i<ppl;i++)
		{
			smallest=-1;
			largest=0;
			for(int j=1;j<=n;j++)
			{
				left=right=0;
				if(!arr[j])
				{
					for(int k=j-1;!arr[k];k--)
					{
						left++;
					}
					for(int k=j+1;!arr[k];k++)
					{

						right++;
					}
					ansmin=min(left,right);
					ansmax=max(left,right);
					if(ansmin>smallest)
					{
						smallest=ansmin;
						largest=ansmax;
						pos=j;
					}
					else if(ansmin==smallest&&ansmax>largest)
					{
						largest=ansmax;
						pos=j;
					}
				}
			}
			arr[pos]=true;
		}
		cout<<"Case #"<<a<<": "<<largest<<" "<<smallest<<"\n";
	}
}
