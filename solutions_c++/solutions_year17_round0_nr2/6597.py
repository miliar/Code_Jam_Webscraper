#include <fstream>
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int currentCount;

vector<int> getLastTidy(unsigned long long int lastN);
int main(){
	FILE *ipf, *opf;

	ipf = fopen("small.in", "r");
	opf = fopen("small.out", "w");


	int T;

	fscanf(ipf, "%d", &T);
	unsigned long long int lastNum, k;
	vector<int> lastTidy;
	int orgT = T;
	while (T--){
		fscanf(ipf, "%lld", &lastNum);
		lastTidy = getLastTidy(lastNum);
		int c = 0;
		vector<int>::iterator it = lastTidy.begin();
		fprintf(opf, "CASE #%d: ", orgT-T);
		// printf("THE SIZE IS  %d\n", lastTidy.size());
		for (;it!=lastTidy.end();it++){
			// cout<<lastTidy.size();
			// scanf("%d",k);
			if (it == lastTidy.begin()&& *it==0){}
				else{
					fprintf(opf, "%d", *it);
				}
			
		
			c++;
		}
		fprintf(opf, "\n");
	}

}

vector<int> getLastTidy(unsigned long long int n){
	cout<<n<<endl;
	int i,j, count;
	unsigned long long int f = n;
	count =0;
	int multFact = 1;
	while (n>0){
		// cout<<count<<endl;

		n= n/10;

		count++;
	}
	currentCount = count;
	vector<int> digits;
	// cout<<count<<endl;
	while (count>0){
		digits.insert(digits.begin(), f%10);
		f = f/10;
		count--;
	}
	bool done = false;
	int iter =0;
	int keepingTrack = 0;
	for (;iter<currentCount-1;iter++){
		if (done){
			
			digits[iter] = 9;
		}
		if (!done){
			if (digits[iter]==digits[iter+1]){
				// cout<<"HERE"<<endl;
				keepingTrack++;
			}
			if (digits[iter]>digits[iter+1]){
				// cout<<keepingTrack<<endl;
				int fff = iter;

				if (keepingTrack==0){
									digits[iter]--;

				}
				while (keepingTrack>0){
					digits[fff]= 9;
					fff--;
					keepingTrack--;
					if (keepingTrack ==0){
						digits[fff]--;

					}
				}





				done = true;
			}else if (digits[iter]<digits[iter+1]){
				// cout<<"SHIT"<<endl;
				keepingTrack = 0;
			}
		}
		

	}
	if(done)
		digits[currentCount-1] = 9;

	return digits;

;}