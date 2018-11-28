#include <iostream>
#include <string>
using namespace std;

int a[1001],b[1001];



int main(){
	//freopen("B-small.in","r",stdin);
	//freopen("B-out.txt","w",stdout);
	int c,cc,t=0,i,ans,k,j,ind=0,sm=0;
	bool indi=true;
	string str;
	
	scanf("%lld",&cc);

	for(c=1 ; c<=cc ; c++){
		cin>>str;
		scanf("%d",&k);
		sm=str.size();
		for(i=0;i<sm-k+1;i++)
		{
			if(str[i]=='-')
				{ind++;
				for(j=0;j<k;j++)
					{
						
						if(str[i+j]=='-') str[i+j]='+';
						else str[i+j]='-';}
						
					}

		}
		//cout<<str<<endl;
		for(i=0;i<str.size();i++){
			if(str[i]=='-')  indi=false;
		}

		if(indi)
		cout << "Case #" << c << ": " << ind << endl;
		else
			cout << "Case #" << c << ": " << "IMPOSSIBLE" << endl;
		
		ind=0;
		indi=true;}
		
		return 1;
	}
