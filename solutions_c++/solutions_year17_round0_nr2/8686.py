#include<bits/stdc++.h>

using namespace std;

bool checkOrdered(long long unsigned N){
	int remR, remL;

	if(N <= 10)
		return true;

	remR = N % 10;
	N /= 10;
	while(N > 0){
		remL =  N % 10;
		if(remL <= remR){
			remR = remL;
		}
		else
			return false;
		N /= 10;
	}
	return true;
}

// long long unsigned checkOrdered(long long unsigned N){
// 	vector<int> unN;
// 	vector<int> sN;
// 	vector<int> result;
// 	long long unsigned num;
// 	int rem;
// 	num = N;
// 	while(num > 0){
// 		rem = num % 10;
// 		num /= 10;
// 		unN.push_back(rem);
// 		sN.push_back(rem);
// 	}
// 	reverse(unN.begin(),unN.end());
// 	sort(sN.begin(), sN.end());

// 	// for (vector<int>::iterator it=unN.begin(); it!=unN.end(); ++it)
//  //    	cout << ' ' << *it;
//  //    cout << endl;
// 	// for (vector<int>::iterator it=sN.begin(); it!=sN.end(); ++it)
//  //    	cout << ' ' << *it;

//     int length = unN.size(), count = 0, flag = 0, f = 0;

//     while(length-- > 0) {
//         if(unN[count] == sN[count])
//         {
//         	result.push_back(unN[count]);
//         	count++;
//         }
//         else
//         {   
//         	if(sN[count] == 0 && unN[count] == 1 && count == 0){
//         		flag = 1;
//         		break;
//         	}
//         	if(f == 0){

//         	if (sN[count] < unN[count])
//         	{
//         		result.push_back(unN[count]-1);
//         		count++;
//         	}
//         	else {
//         		result.push_back(9);
//         		count++;
//         		f = 1;
//         	}
//         	}

//         	else{
//         		result.push_back(9);
//         		count++;
//         	}
//         }
//     }

//     long long unsigned res = 0;
    
//     if(flag == 1){
//     	res = pow(10,length);
//     	return res -  1;
//     }
    
//     for (vector<int>::iterator it=result.begin(); it!=result.end(); ++it)
//     	 res = res * 10 + *it;

// 	return res;
// }


// long long unsigned checkOrdered(long long unsigned N){
// 	vector<int> unN;
// 	vector<int> sN;
// 	vector<int> result;
// 	long long unsigned num;
// 	int rem;
// 	num = N;
// 	while(num > 0){
// 		rem = num % 10;
// 		num /= 10;
// 		unN.push_back(rem);
// 		sN.push_back(rem);
// 	}
// 	reverse(unN.begin(),unN.end());	

// 	int length = unN.size();
// 	while(length-- > 1) {
// 	    if(unN[length-1] > unN[length]){
// 	    	unN[length] = 9;
// 	    	if((length+1) != unN.size()){
// 	    		unN[length+1] = 9;
// 	    	}
// 	    	if (unN[length-1] != 0)
// 	    	{
// 	    		unN[length-1] = unN[length-1] - 1;	
// 	    	}	    	
// 	    }
// 	}
// 	if(unN.size() > 1)
// 		unN[unN.size() -  1] = 9;

//     long long unsigned res = 0;
// 	for (vector<int>::iterator it=unN.begin(); it!=unN.end(); ++it)
//     	res = res * 10 + *it;

// 	return res;
// }

int main(int argc, char const *argv[])
{

	int T, count = 1;
	long long unsigned N;

	freopen ("B-small-attempt1.in","r",stdin);
	freopen ("B-small-attempt1.out","w",stdout);

	cin >> T;
	while(T-- > 0){
		cin >> N;
		while(!checkOrdered(N)) {
			N--;		    
		}		
		cout << "Case #" << count++ << ": " << N << endl;
	}
	return 0;
}