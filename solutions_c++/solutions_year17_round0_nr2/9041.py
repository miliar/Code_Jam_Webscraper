#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {

	//input
	//---------------------

		//the number of test cases
		int T;

		//input data
		unsigned long long N[100];
		//int N[100];
		//output data
		unsigned long long  Out[100];

		int d[19];
 
		cin >> T;

		for(int i=0; i<T; i++){
			cin >> N[i];
		}

		//-----Test-----
		//T=100;

		//for(int i=0; i<T; i++){
			//N[i]=(i+1)*100;
		//}
		//--------------

		//cout << "T" << T << endl;
		//for(int i=0; i<T; i++){
			//cout << "Case"<< i+1 << ":" << N[i] << endl;
		//}

	//---------------------

	unsigned long long  q;
	int flag = 0;
	for(int i=0; i<T; i++)
	{

		//cout << "Case #" << i+1 << endl;
		//cout << "N[" << i << "] "  << N[i] << endl;
		flag=0;
		for(unsigned long long j=N[i]; 0<j; j--){

			q = j;
			int digit=0;
			//cout << "j "  << j << endl;
			//cout << "q "  << q << endl;
			while(q!=0){
				d[digit] = q%10;
				//cout << q << "%10 " << q%10 << endl;
				//cout << q << " /10 " << q/10 << endl;
				q = q/10;
				digit++;
			}

			//for(int k=0; k<digit ; k++){
				//cout << d[k];
			//}
			//cout << endl;

			int count=0;

		    if(digit==1){
				Out[i] = j;
				break;
			}
			for(int k=digit-1; 0<k; k--){
				//cout << d[k-1] << " " << d[k]<< endl;
				if(d[k-1] >= d[k]){
					count++;
				}
				//cout << " count " << count << endl ;
				//cout << " digit " << digit << endl ;
				if(count + 1 == digit ){
					Out[i] = j;
					flag=1;
					break;
				}
			}
			if(flag==1){
				break;
			}
		}
	}


	//output
	//---------------------
	for(int i=0; i<T; i++){
		if(i<T-1){
			//cout << "N[" << i << "] : "<< N[i] << endl;			
			cout << "Case #" << i+1 << ": "<< Out[i] << endl;
		}else{
			//cout << "N[" << i << "] : "<< N[i]; 
			cout << "Case #" << i+1 << ": "<< Out[i];
		}
	}

	//---------------------

    	return 0;
}
