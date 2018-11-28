#include <iostream>
#include <fstream>
#include <set>

using namespace std;

void process(uint64_t n, uint64_t k, ostream &out);

int main(int argc, char **argv){
	ifstream in(argv[1]);
	ofstream out("c.out");
	int num;
	in>>num;

	for(int i=0;i<num;i++){
		uint64_t n,k;
		in>>n>>k;

		out<<"Case #"<<(i+1)<<": ";
		process(n, k, out);
	}

	in.close();
	out.close();

	return 0;
}

void process(uint64_t n, uint64_t k, ostream &out){
	multiset<uint64_t> l;
	l.insert(n);
	uint64_t lastMin, lastMax;
	for(uint64_t i=0;i<k;i++){

		
		auto end=l.end();
		end--;
		uint64_t num=*end;
		l.erase(end);

		if(num%2==0){
			num/=2;
			l.insert(num);
			l.insert(num-1);
			lastMax=num;
			lastMin=num-1;
		}else{
			num/=2;
			l.insert(num);
			l.insert(num);
			lastMax=lastMin=num;
		}
	}
	out<<lastMax<<" "<<lastMin<<endl;
}