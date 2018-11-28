

#include <iostream>
#include <algorithm>
#include <string>

int main() {

	std::ios_base::sync_with_stdio(false);
/*
	freopen("inputL.in","r",stdin);
	freopen("outputL.txt","w",stdout);
*/
    long long t;
	std::cin >> t;
    
	for(long long z = 1; z <= t; z++)
	{
		std::string a;
		std::cin >> a;
		
		for(long long i=0; a[i]!='\0' and a[i+1]!='\0'; i++)
		{
			if(a[i]>a[i+1]) 
			{
				while(a[i]==a[i-1])
						i--;
				a[i]--;
				i++;
				while(a[i]!='\0') 
				{
					a[i]='9';
					i++;
				}
				break;
			}
		}
        a.erase(0, a.find_first_not_of('0'));
		std:: cout <<"Case #"<< z << ": " <<  a << "\n";
    }
}
