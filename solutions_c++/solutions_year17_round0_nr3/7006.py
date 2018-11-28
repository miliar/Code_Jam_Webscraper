#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	for (int testCase = 1; testCase <= t; ++testCase)
	{
		long n,k;
		cin>>n>>k;


		multiset <long> occupiedStalls;
		vector <bool>  occupied(n+2,false);
		occupied[0] =true;
		occupied[n+1] = true;

		occupiedStalls.insert(0);
		occupiedStalls.insert(n+1);
		long m = n/2;

		if(n%2!=0) m++;
		if(n==1) m=1;
		occupied[m]=true;
		occupiedStalls.insert(m);

    long mid = m;
    for(int person = 1 ; person < k ;person++){

        auto iterate = occupiedStalls.begin();
        iterate++;
        long matestCase = 0;
        mid = 0;

		while(iterate != occupiedStalls.end()){

            iterate--;
            int a = *(iterate);
            iterate++;
            int b = *(iterate);

            if(matestCase < b-a-1){

                    matestCase = b-a-1;
                    mid = (a+b)/2;
            }
            iterate++;
		}

		occupiedStalls.insert(mid);
		occupied[mid]=true;
    }


    int ls=0,rs=0;

    int i = mid-1;
    while(i>=0 && occupied[i] != true ){
        ls++;
        i--;
    }

    int j = mid+1;
    while( j<= n+1 && occupied[j] != true ){
        rs++;
        j++;
    }

    if(ls>rs)
    cout<<"Case #"<<testCase<<": "<<ls<<" "<<rs<<endl;
    else
    cout<<"Case #"<<testCase<<": "<<rs<<" "<<ls<<endl;


	}



	return 0;
}
