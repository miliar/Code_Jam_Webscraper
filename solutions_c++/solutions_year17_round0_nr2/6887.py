#include<iostream>
using namespace std;

int countDigits(long long int);
void printTidy(int *, int, int);

int main(){
    int t;
    cin >> t;

    for(int i = 0; i < t; i++){
	long long int n = 0;
	cin >> n;
	int digits = countDigits(n);
        int *array = new int[digits];
        for(int i = digits-1; i >= 0; i--){
	    array[i] = n % 10;
	    n = n/10;
	}
	printTidy(array, digits, i+1);
	cout<<endl;
    }
}

int countDigits(long long int n)
{
    int digits = 0;
    while(n != 0){
	n = n/10;
	digits++;
    }
return digits;
}

void printTidy(int *array, int digits, int caseNumber){
	int i = 0;
	if(digits > 1){
		while(array[i] <= array[i+1] && (i < digits-1)){
		    i++;
		}
		if(i < digits-1)
		{
		        while(array[i] == array[i-1]){
			    i--;
			}

			array[i] = array[i] - 1;i++;

			while(i < digits){
		        	array[i] = 9;i++;
			}
		}
		cout<<"Case #"<<caseNumber<<": ";
		for(int i = 0; i < digits; i++){
		    if (array[i])
        		cout<<array[i];
		}
	}
	else{
	    cout<<"Case #"<<caseNumber<<": "<<*array;
	}
}
