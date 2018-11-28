#include <iostream>
#include <fstream>
using namespace std;

bool check(int a)
{

	int flag=1;
	while(a/10>0)
	{
		if(a%10<(a/10)%10)
		{
			flag=0;
			break;
		}
		a/=10;
	}
	return flag;
}

int main ()
{
    ifstream ifs;
    ifs.open("input.txt");
    int n;
    ifs >> n;
    long tidy;
    int c;
    long temp;
    for (int i = 0; i < n; i++)
    {
        ifs >> tidy;
        temp = tidy;
        c = 0;
        for (long i = tidy; i >=0; i--) {
            if (check(i))
            {
                temp=i;
				break;
            }
        }
        cout << "Case #" << i+1 << ": " << temp << endl;
    }
    return 0;
}
