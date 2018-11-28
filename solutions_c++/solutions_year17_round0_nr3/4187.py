#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <sstream>
#include <vector>
#include <sstream>
#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <numeric>
#include <tuple>

using namespace std;


int main()

{
    freopen("C-small-2-attempt0.in.txt","rt",stdin);
	freopen("C-small-2-attempt0.out.txt","wt",stdout);

    int T;
    cin >> T;
    cout.precision(18);
    long K, N;
    long Ls=0, Rs=0;
	for (int caseN = 1; caseN <= T; ++caseN) {
		cout << "Case #" << caseN << ": ";
		cin>>N>>K;
		priority_queue<long> free;
		long y=0,z=0; //y is max(LS, RS), and z is min(LS, RS)
		free.push(N);
		if(K==N)
			cout<<0<<" "<<0<<endl;

		else if(K==1){
			if(N%2==1)
				cout<<N/2<<" "<<N/2<<endl;
			else
				cout<<N/2<<" "<<N/2-1<<endl;
		}
		else{
			while (!free.empty() && K>0){
				Rs=free.top();
				free.pop();
				if(Rs==1)
				{
					y=0; z=0;
					break;
				}
				//cout<<K<<"finding "<<Rs<<"-";
				
				y=Rs/2;
				if(Rs%2==1)
					z=Rs/2;
				else z=Rs/2-1;
				free.push(y);
				free.push(z);
				K--;

				//cout<<y<<"and"<<z<<endl;
			}

			cout<<y<<" "<<z<<endl;
		}

	}
	fclose(stdin);
	fclose(stdout);
	return 0;

}
