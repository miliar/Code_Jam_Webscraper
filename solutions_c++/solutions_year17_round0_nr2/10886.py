#include <iostream>
#include <fstream>

using namespace std;
ofstream output;
int l = 0;

bool callbacknum(int *num , int i)
{
	if (num[i] == 0 && i < l)
	{
		if(callbacknum(num,i+1))
		{
			num[i] = 9;
			return true;
		}
		else{
			return false;
		}
	}
	else if(l == i)
	{
		return false;
	}
	else
	{
		num[i]--;
		return true;
	}

}


bool check_num(int n , int lvl){

    if(n/10 < 0)
    {
		output << "Case #" << lvl << ": " << n << endl;
		return true;
	}

	int sep = n;
	while(sep > 0)
	{
		sep = sep /10;
		l++;
	}

	sep = n;
	int nums[l];
	for (int i = 0 ; i < l; ++i)
	{
		nums[i] = sep%10;
		sep = sep/10;
	}


	for (int i = 0; i < l; ++i)
	{

		if ((nums[i] < nums[i+1] && i < l - 1) || (nums[i] == 0 && i == 0))
		{

			if (i == 0 )
			{
				nums[i] = 9;
				callbacknum(nums , i+1);
			}
			else if(i < l - 1)
			{
                if(nums[i-1] != 9 )
                {
                    return false;
                }
				nums[i] = nums[i-1];
				callbacknum(nums , i+1);
			}

		}
	}

		bool ok = true;



		for (int j = 0; j < l-1; ++j)
		{
			if (nums[j] < nums[j+1])
			{
				return false;
			}
		}


            sep = 0;
            for (int i = 0 , j = 1; i < l; ++i , j = j*10)
            {
                sep = sep + (nums[i] * j);
            }
			output << "Case #" << lvl << ": " << sep << endl;
			return true;



}

int main() {
output.open("output.txt");
ifstream inp("inp.in");
	int t , n;
	inp >> t;
	for (int i = 0; i < t; ++i) {
		inp >> n;
		if(!check_num(n , i+1))
            check_num((n - (n%10)), i+1);

	}

	output.close();
	return 0;
}
