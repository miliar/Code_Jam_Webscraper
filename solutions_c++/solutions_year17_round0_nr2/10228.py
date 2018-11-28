# include <iostream>

using namespace std;

int main()
{
	int T,N;

	cin >> T;
	if (T <1 || T > 100)
	{
		return 0;
	}
	else
	{
		for(int i = 1 ; i <= T ;i ++)
		{
			cin >> N ;
			if(N < 1 || N > 1000)
			{
				return 0;
			}
			else
			{
				int flag =1;
				while(flag > 0)
				{
					if(N < 10)
					{
						cout << "Case #" << i << ": " <<N<< endl;
						flag =0;
					}
					else
					{
						 int res = N;
						 int val = 0;
						 int b = -1;
						 int per_flag = 0;
						 int c1 =0;
						 int c2 =0;
						 int check_flag = 0;
						 while(res  > 0)
						 {
						 	val = res % 10;
						 	res = res /10;
						 	if (b == -1)
						 	{
						 		b = val;

						 		c1++;
						 	} 
						 	else
						 	{
						 		if(b >= val)
						 		{
						 			b = val;
						 			c1++;
						 		}
						 		else
						 		{
						 			check_flag = 1;
						 			break;
						 		}
						 	}
						 	c2++;
						 }
						 if(res == 0 && c1 == c2 && check_flag == 0)
						 {
						 		cout << "Case #" << i << ": " <<N<< endl;
								flag =0;
						 }
						 else
						 {
						 	N --;
						 }
					}
				}
			}
		}
	}
}