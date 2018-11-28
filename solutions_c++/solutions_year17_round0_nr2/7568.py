#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int main() {
  int t, n, m;
  int array[25];
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  getchar();
  for (int i = 1; i <= t; ++i) {
	char temp;
	int it=0;
	while((temp=getchar())!='\n'){
		array[it]=temp - '0';
		it++;
	}
	array[it]=-1;
	int len = it-1;
	int x = len;
	while(x!=0){
		//8700000000
		//604-1
		if(array[x]==0)
		{
			while(array[x]==0){array[x]=9;x--;}
			array[x]--;
			x++;
			while(array[x]!=-1)array[x++]=9;
                        x--;
		}
		else if(array[x]>=array[x-1])x--;
		else {
		  array[x-1]--;
		  while(array[x]!=-1)array[x++]=9;
			x--;
		}
	}
  	cout << "Case #" << i << ": ";
	for(int i=0; array[i]!=-1 ;i++){
                if(array[i]!=0)cout << array[i];
        }
	cout << endl;
  }
  return 0;
}
