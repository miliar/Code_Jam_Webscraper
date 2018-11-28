#include <iostream>
#include <cstdio>
#include <fstream> 
#include <set>

using namespace std;

multiset<long long> S;

long long getAnswer(long long n, long long k)	{
	S.clear();
	S.insert(n);
	while(k > 1)	{
		

		// cout<<"printing set"<<endl;
		// for(multiset<long long>::iterator it = S.begin() ; it != S.end() ; ++it)	{
		// 	cout<<*it<<" ";
		// }
		// cout<<endl;


		--k;
		long long maxVal = *(S.rbegin());
		S.erase(prev(S.end()));
		S.insert(maxVal/2);
		S.insert((maxVal-1)/2);
	}
	return *(S.rbegin());
}

int main()	{

	int t,caseNum = 0;
	long long n,k;
	ifstream in; in.open("/Users/paliws/Downloads/input.txt");
	ofstream out; out.open("/Users/paliws/Downloads/output.txt");
	in>>t;
	while(t--)	{
		++caseNum;
		in>>n>>k;
		long long answer = getAnswer(n,k);
		out<<"Case #"<<caseNum<<": "<<answer/2<<" "<<(answer-1)/2;
		if(t != 0)	{
			out<<endl;
		}
	}
	in.close();
	out.close();
	return 0;
}