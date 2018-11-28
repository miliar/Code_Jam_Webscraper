#include<iostream>

using namespace std;

int main()
{
	
	int mk = 0;
	int b = 0;
	cin >> b;
	while (b--)
	{
		int p = 0;

		int answer = 0;
		int s = 0;
		int n = 0;
		int k = 0;

		cin >> p;
		while(p>0)
		{
	

			  answer = 0;
			  s = 0;
		      n = 0;
			  k = 0;


			answer = p;
			n = p;
			s = p;


			while (n > 0)
			{

				n = n / 10;
				k++;
			}
	


			if (k == 4)
			{
				int z, l, m;
				z = 0;
				l = 0;
				m = 0;
				z = s % 10;
				s = (s / 10);
				l = s % 10;
				s = s / 10;
				m = s % 10;
				s = s / 10;

			if (((z > l) || (z == l)) && ((l > m) || (l == m)) && ((m > s) || (m == s)))
				{
					mk++;
					cout << "Case #" << mk << ": " << answer << endl;
					break;
				}

			}
			if (k == 3)
			{
				int  l, m;

				l = 0;
				m = 0;


				l = s % 10;
				s = s / 10;
				m = s % 10;
				s = s / 10;

				if (((l > m) || (l == m)) && ((m > s) || (m == s)))


				{
					mk++;
					cout << "Case #" << mk << ": " << answer << endl;
					break;
				}
			}

			if (k == 2)
			{
				int  m;

				m = 0;

				m = s % 10;
				s = s / 10;

				if ((m > s) || (m == s))
				{
					mk++;
					cout << "Case #" << mk << ": " << answer << endl;
					break;
				}

			}

			if (k == 1)
			{
				mk++;
				cout << "Case #" << mk << ": " << answer << endl;
				break;
				
			}
			p--;
		}
	}
	
 	return 0;
}
