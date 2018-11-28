#include <iostream>
#include <fstream>
#include <list>
#include <cstdio>
#include <sstream>
#include <string>

using namespace std;

list<char> makeNines(list<char> source){
	list<char> res;
	for(int i = 0; i < source.size(); i++)
		res.push_back('9');
	return res;
}

list<char> decrease(list<char> source){
	char last = source.back();
	source.pop_back();
	if(last > '0'){
		last -= 1;
		source.push_back(last);
		return source;
	}
	else{
		if(source.size() == 0)
			return source;
		source = decrease(source);
		source.push_back('9');
		return source;
	}
}

string lastTidy(string number){
	list<char> left, right;
	for(int i = 0; i < number.size(); i++){
		left.push_back(number.at(i));
	}

	right.push_front(left.back());
	left.pop_back();

	while(left.size() > 0){
		char last = left.back();
		//left.pop_back();
		char first = right.front();
		if(last > first){
			right = makeNines(right);
			left = decrease(left);
			last = left.back();
			left.pop_back();
			if(last == '0' && left.size() == 0)
                break;
			right.push_front(last);
		}
		else{
            left.pop_back();
            right.push_front(last);
		}
	}


	string res;
	while(right.size() > 0){
		res += right.front();
		right.pop_front();
	}
	return res;
}

int main(){
    string inname = "B-large.in";
    string outname = "B-large.out";
    ifstream infile(inname);
    ofstream outfile(outname);

    int T;
    infile >> T;
    string number;
    string res;
    for(int i = 1; i <= T; i++){
        infile >> number;
        res = lastTidy(number);
        outfile << "Case #" << i <<": " << res;
        if(i < T)
            outfile << endl;
    }
    infile.close();
    outfile.close();
	return 0;
}
