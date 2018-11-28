#include <iostream>
#include <sstream>
#include <string>
#include <string.h>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <iomanip>
#include <unordered_map>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
template <class T> inline string itos(T n) {return (n)<0?"-"+itos(-(n)):(n)<10?(string)("")+(char)('0'+(n)):itos((n)/10)+itos((n)%10);}
template<class T>T my_pow(T n,T p){if(p==0)return 1;T x=my_pow(n,p/2);x=(x*x);if(p&1)x=(x*n);return x;} ///n to the power p

int case_number;
#define printg case_number++, printf("Case #%d: ",case_number), printf
#define gout case_number++, printf("Case #%d: ",case_number), cout
#define ulld unsigned long long int

#define INF (1<<29)

bool istidy(ulld n)
{
	int digit=-1;
	while(n!=0){
		if(digit!=-1 && digit<n%10) return false;
		digit=n%10;
		n=n/10;
	}
	return true;
}

void main2(void){
	ulld n;
	cin>>n;
	if(n<10){
		gout<<n<<endl;
		return;
	}
	ulld gN=n;
	ulld digit=INF;
	ulld pos=0;
	ulld curr_n=0;
	ulld loop_n=n;
	int curr_digit=n%10;
	while(loop_n!=0){
		curr_digit=(pos==0)?curr_digit:(n/my_pow<ulld>(10,pos))%10;
		if(digit<curr_digit){
			gN-=(curr_n+1);
			n=gN;
		}
		digit=(n/my_pow<ulld>(10,pos))%10;
		++pos;
		curr_n=n%my_pow<ulld>(10,pos);
		loop_n=loop_n/10;
	}
	gout<<n<<endl;
}

int main(void){
	int number_of_test_cases,i;
	scanf("%d",&number_of_test_cases);
	REP(i,number_of_test_cases) main2();
	return 0;
}
