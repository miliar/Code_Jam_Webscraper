#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int numCase(string &content){
	int T = content.find(' ');
	int num=0;
	// max case: 1 ≤ T ≤ 100

	switch (T){
		case 1: num=content[0]-'0';
		break;

		case 2: num=(content[0]-'0')*10+(content[1]-'0');
		break;

		case 3: num = 100;
		break;
	}
	content.erase(0, T+1);
	return num;
}

int sToInt(string s){
	int digit = s.size();
	int num=0;
	// max case: 1 ≤ T ≤ 1000
	switch (digit){
		case 1: num=s[0]-'0';
		break;

		case 2: num=(s[0]-'0')*10+(s[1]-'0');
		break;

		case 3: num = (s[0]-'0')*100+(s[1]-'0')*10+(s[2]-'0');
		break;

		case 4: num=1000;
		break;
	}
	return num;
}

int sToIntArray(string content, int *&p){
	int length = content.find(' ');
	p = new int[length];
	for (int i=0; i<length;i++)
	{
		char c = content[i];
		if(c=='+'){p[i]=1;}
		if(c=='-'){p[i]=0;}
	}
	return length;
}
bool checkDone(int *p, int lengthArr){
	for(int i=0; i<lengthArr;++i){
		if(p[i]==0){
			return false;
		}
	}
	return true;
}
void flipping(int *&p, int flipConstant, int start){
	for(int i = start; i<start+flipConstant;++i){
		if(p[i]==0){
			p[i]=1;
		}
		else{
			p[i]=0;
		}
	}
}

int shiftingArray(int *&p, int flipConstant, int lengthArr){
	int count = 0;
	for(int i=0; i<lengthArr-flipConstant+1;++i){
		if(p[i]==0){
			flipping(p, flipConstant, i);
			count++;
		}
	}

	if(checkDone(p, lengthArr)){return count;}
	else return 0;
	
}

void outputResult(int caseID, int answer, int caseNum){
	ofstream fout;
	fout.open("C:\\Users\\tim12\\Desktop\\output.txt", ios::app);
	if(caseID!=3&&answer!=0){caseID=1;}
	if(caseID!=3&&answer==0){caseID=2;}
	switch(caseID){
		case 1: fout << "Case #"<<caseNum+1<<": "<< answer<<endl;
		break;
		case 2: fout << "Case #"<<caseNum+1<<": IMPOSSIBLE"<<endl;
		break;
		case 3: fout << "Case #"<<caseNum+1<<": 0"<<endl;
		break;
	}
		fout.close();
	}

	int main (){
	//opening input file
		ifstream input;
		string line;
		string content;
	input.open("C:\\Users\\tim12\\Desktop\\A-large.in");
	while(input >> line) {
		content += line + ' ';
	}

	int T = numCase(content);
	int * p;

	for(int i=0; i<T;i++){

		//collecting info
		int k = sToIntArray(content, p);
		content.erase(0,k+1);
		string s = content.substr(0, content.find(' '));
		int flipConstant = sToInt(s);		
		content.erase(0,content.find(' ')+1);

		int answer = 0;
		int caseID = 0;
		if(checkDone(p, k)){caseID = 3;}
		answer = shiftingArray(p, flipConstant, k);
		outputResult(caseID, answer, i);
	}
}
