#include <iostream>
typedef long long int ll;
using namespace std;

ll t,n,k;
ll ps, pr;
ll psd, prd;

int main()
{
	cin >> t;

	for (int i = 1; i <= t; ++i)
	{
		cin >> n >> k;
		cout << "Case #" << i << ": ";

		int l = 0;
		ll p = 0;

		if (n%2 == 0)
		{
			ps = n;
			pr = 0;

			psd = 1;
			prd = 0;
		}
		else
		{
			ps = 0;
			pr = n;

			psd = 0;
			prd = 1;
		}

		if (k == 1)
		{
			if (n == 1)
			{
				cout << "0 0" << endl;
			}
			else if (n%2 == 0)
			{
				cout << n/2 << ' ' << n/2-1 << endl;
			}
			else
			{
				cout << (n-1)/2 << ' ' << (n-1)/2 << endl;
			}
		}

		while (k>1)
		{
			l++;

			if (psd > 0)
			{
				ll tmp = ps/2;

				if (tmp>1)
				{
					if (pr<ps)
					{
						if (tmp%2 == 0)
						{
							ps = tmp;
							psd = psd;

							pr = tmp-1;
							prd = (1<<l)-psd;
						}
						else
						{
							pr = tmp;
							prd = psd;

							ps = tmp-1;
							psd = (1<<l)-prd;
						}
					}
					else
					{
						if (tmp%2 == 0)
						{
							pr  = tmp-1;
							prd = psd;

							ps = tmp;
							psd = (1<<l)-prd; 
						}
						else
						{
							ps = tmp-1;
							psd = psd;

							pr = tmp;
							prd = (1<<l)-psd;
						}
					}
				}
				else
				{
					pr = 1;
					prd = psd;

					ps = 0;
					psd = 0;
				}
			}
			else
			{
				ll tmp = (pr-1)/2;
			
				if (tmp%2 == 0)
				{
					ps = tmp;
					psd = (1<<l);

					pr = 0;
					prd = 0;
				}
				else
				{
					pr = tmp;
					prd = (1<<l);

					ps = 0;
					psd = 0;
				}
			}

			//cout << "PSD: " << psd << " PS: " << ps << " PRD: " << prd << " PR: " << pr << endl;

			if (k < (1<<(l+1)))
			{
				//cout << "PSD: " << psd << " PS: " << ps << " PRD: " << prd << " PR: " << pr << endl;
				if (psd == 0)
				{
					cout << (pr-1)/2 << ' ' << (pr-1)/2 << endl;
				}
				else if (prd == 0)
				{
					cout << ps/2 << ' ' << ps/2-1 << endl;
				}
				else
				{
					if (ps<pr)
					{
						//cout << ((1<<l)-1+psd) << endl;
						if ((1<<l)-1+prd < k)
						{
							cout << ps/2 << ' ' << ps/2-1 << endl;
						}
						else
						{
							cout << (pr-1)/2 << ' ' << (pr-1)/2 << endl;
						}
					}
					else
					{
						if ((1<<l)-1+psd < k)
						{
							cout << (pr-1)/2 << ' ' << (pr-1)/2 << endl;
						}
						else
						{
							cout << ps/2 << ' ' << ps/2-1 << endl;
						}
					}
				}
				break;
			}
		}
	}
}