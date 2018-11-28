#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    int T;
    fstream of("B-small-attempt0.in", ios::in);
    of>>T;
	fstream out("out.txt", ios::out);
    for(int a0 = 0; a0 < T; ++a0)
	{
		long long num;
		of>>num;
		for(int i = num; i >= 0; --i)
		{
			int arr[18] = {0};
			int j = i, k = 0;
			while(j > 0)
			{
				arr[k++] = j % 10;
				j /= 10;
			}
			int flag = 0;
			for(j = 0; j < k - 1; ++j)
				if(arr[j] < arr[j + 1])
			{
				flag = 1;
				break;
			}
			if(flag == 0)
			{
				out<<"Case #"<<a0 + 1<<": "<<i<<"\n";
				break;
			}
		}
	}
}
