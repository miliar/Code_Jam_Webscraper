#include <iostream>

using namespace std;

//Function declarations
long long check(long long);

//////////////////////////////////////////////////
int main()
{
	int i,T;
	long long N, res;
	cin >> T;
  for (i=1; i<=T; i++){
  	cin >> N;
  	res = check(N);
  	cout << "Case #" << i << ": " << res <<endl;
  }
  
  return 0;
}//end main
//////////////////////////////////////////////////

long long check(long long N){
	int temp=9;
	long long wrong=1;
	long long neki=N;
	while (neki!=0){
		if (neki%10<=temp){
			temp=neki%10;
			neki = neki/10;
			wrong *=10;
			continue;
		}
		return check(N-N%wrong-1);
	}
	return N;
}
















