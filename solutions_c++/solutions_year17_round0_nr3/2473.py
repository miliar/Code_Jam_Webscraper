#include <iostream>
#include <cstdlib>
#include <cmath>
#include <set>
using namespace std;

struct node{
	long long int value;
	long long int occur;
};
typedef struct node node;

struct comb{
	node a;
	node b;
};
typedef struct comb comb;

int main(void)
{
	int t, case_no;
	cin >> t;
	for(case_no = 1; case_no <= t;case_no++)
	{
		long long int n, k, persons = 1;
		cin >> n >> k;
		
		if(k == 1)
		{
			long long int mean = (n % 2)?(n+1)/2:n/2;
			cout << "Case #" << case_no << ": ";
			cout << max(mean-1, n-mean) << " " << min(mean-1, n-mean) << endl;
			continue;
		}
		
		comb* arr = (comb*) malloc (65 * sizeof(comb));
		long long int mean = (n % 2)?(n+1)/2:n/2;
		arr[0].a.value = max(mean-1, n-mean);
		arr[0].a.occur = 1;
		arr[0].b.value = min(mean-1, n-mean);
		arr[0].b.occur = 1;
		persons += arr[0].a.occur + arr[0].b.occur;
		int i = 0;
		if(persons >= k)
			goto neeche;
			
		for(i = 1;i < 65;i++)
		{
			long long int prev1 = arr[i-1].a.value, prev2 = arr[i-1].b.value;
			long long int occur1 = arr[i-1].a.occur, occur2 = arr[i-1].b.occur;
			long long int mean1 = (prev1 % 2)?(prev1+1)/2:prev1/2;
			long long int mean2 = (prev2 % 2)?(prev2+1)/2:prev2/2;
			node m[4];
			m[0].value = mean1 - 1; m[0].occur = occur1;
			m[1].value = prev1 - mean1; m[1].occur = occur1;
			m[2].value = mean2 - 1; m[2].occur = occur2;
			m[3].value = prev2 - mean2; m[3].occur = occur2;
			//cout << endl << prev1 << " " << occur1 << " " << prev2 << " " << occur2; 
			for(int j = 0;j < 4;j++)
				for(int l = j+1;l < 4;l++)
					if(m[j].value == m[l].value)
						m[j].occur += m[l].occur;
			arr[i].a.value = m[0].value;
			arr[i].a.occur = m[0].occur;
			int j;
			for(j = 1;j < 4;j++)
				if(m[j].value != m[0].value)
				break;
			if(j == 4)
			{
				j = 0;
				arr[i].b.value = m[j].value;
				arr[i].b.occur = 0;
			}
			else
			{	
				arr[i].b.value = m[j].value;
				arr[i].b.occur = m[j].occur;
			}
			persons += arr[i].a.occur + arr[i].b.occur;
			//cout << " " << persons << endl;
			if(persons >= k)
			break;
 		}
		
		neeche:
		long long int kaam;
		long long int diff = k - (persons - arr[i].a.occur - arr[i].b.occur);
		//cout << endl << arr[i].a.occur << " " << arr[i].b.occur << " " << diff << endl;
		if(arr[i].a.value > arr[i].b.value)
			kaam = (diff > arr[i].a.occur)?arr[i].b.value:arr[i].a.value;
		else
			kaam = (diff > arr[i].b.occur)?arr[i].a.value:arr[i].b.value;
		//cout << endl << kaam << endl;	
		mean = (kaam%2)?(kaam+1)/2:kaam/2;
		cout << "Case #" << case_no << ": ";
		cout << max(mean-1, kaam-mean) << " " << min(mean-1, kaam-mean) << endl;
	}
	return 0;
}