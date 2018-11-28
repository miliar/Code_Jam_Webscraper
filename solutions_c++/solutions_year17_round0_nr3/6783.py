/*
	ID: reagankan
   Lang: c++11
	Google Code Jam 2017
   Qualification Round 
   Problem C. Bathroom Stalls
*/
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <unordered_set>

using namespace std;

int NumCases;
int CURR_NUM = 6;
int FACTOR = 77;
unsigned long long N = 0ull, K = 0ull;

void printv(vector <int> vect)
{
	for(int ii = 0; ii < vect.size(); ii++)
 	{
		 cout << "vector[" << ii << "]: " << vect[ii] << endl;
 	}
}
void printv(vector <int> vect, int caseNum)
{
	if(caseNum == CURR_NUM){printv(vect);}
}
void printv(vector <int> vect, int caseNum, int i)
{
	if(caseNum == CURR_NUM && i%FACTOR == 0){printv(vect);}
}
void printSects(vector<vector<int>> v)
{
	for(int i = 0; i < v.size(); i++)
	{
		cout << "sects[" << i << "].size(): " << v[i].size() << endl;
		cout << "start: " << v[i].front() << " end: " << v[i].back() << endl;
	}
}
void printSects(vector<vector<int>> v, int caseNum)
{
	if(caseNum == CURR_NUM){printSects(v);}
}
vector<int> largestSect(vector<vector<int>> v, int caseNum)
{
	if(caseNum == CURR_NUM){/*cout << "l-------startLargestSect...\n";*/}
	unsigned long Mx = 0ul; int idx = -1;

	for(int i = 0; i < v.size(); i++)
	{
		if(caseNum == CURR_NUM){/*cout << "sects[" << i << "].size(): " << v[i].size() << endl;
	cout << "start: " << v[i].front() << " end: " << v[i].back() << endl;*/}
		
		/*if(Mx == v[i].size())
		{
			if(caseNum == CURR_NUM){cout << "CONTINUE at size: " <<  v[i].size() << endl;}
				continue;
		}*///ensure leftmost section
		
		Mx = max(Mx, v[i].size());
		if(Mx == v[i].size()){idx = i;}
		
		//if(caseNum == CURR_NUM){cout << "MX == " << Mx << endl << "\t idx: " << idx << endl;}
	}
	if(caseNum == CURR_NUM)
	{	
		/*cout << "-----\nCHOSEN sect\n-----\n";
		cout << "chosen[" << idx << "].size(): " << v[idx].size() << endl;
		cout << "start: " << v[idx].front() << " end: " << v[idx].back() << endl;
	cout << "endlargestSect--------------\n";*/}
	return v[idx];
}
vector<vector<int>> sections(vector<int> v)
{
	vector<vector<int>> ret;
	vector<int> sect; 
	int past = -1, cnt = 0;
	vector<int>::iterator iter = v.begin(); 
	while ((iter =  find(iter, v.end(), 0)) != v.end()) 
	{ 
		int idx = distance(v.begin(), iter);  
	
		//cout << past << " " << idx << endl;
		if(sect.empty() && past == -1)
			{sect.push_back(idx); /*cout << "create sect\n";*/cnt++;}
		else if(past == sect.back() && past + 1 == idx)
			{sect.push_back(idx); /*cout << "continue sect\n";*/}
		else if(past == sect.back() && past + 1 != idx)
			{ret.push_back(sect); sect.clear(); sect.push_back(idx); /*cout << "new sect\n";*/ cnt++;}
      //printv(sect); cout << "==========\n";
		past = idx;
		iter++; 
	}
   if(cnt != ret.size())
	{
		ret.push_back(sect);
	}
	return ret;
}
pair<int,int> LR(vector<vector<int>> &v, int lastStall)
{
	pair<int,int> finalLR;
	vector<int> lr;
	int ds[] = {-1,1};
	for(int s = 0; s < 2; s++)
	{
		for(int i = 0; i < v.size(); i++)
		{
			if(lastStall+ds[s] == v[i].front() || lastStall+ds[s] == v[i].back())
			{
				lr.push_back(v[i].size());
			}
		}
	}
	//cout << "lr.size(): " << lr.size() << endl;
	int size = lr.size();
	if(size == 0)
	{
		finalLR = make_pair(0,0);
	}
	else if(size == 1)
	{
		finalLR = make_pair(lr[0],0);
	}
	else if(size == 2)
	{
		finalLR = make_pair(lr[0],lr[1]);
	}
	return finalLR;	
}
void bathroom_stalls(ifstream &fin, ofstream &fout, int caseNum)
{
	fin >> N >> K;
	//if(caseNum == CURR_NUM){cout << "Case #" << caseNum << endl;
	//cout << "N: " << N << " K: " << K << endl;}
	//setup bathroom
	vector<int> bathroom(N+2, 0); bathroom[0] = 1; bathroom[N+1] = 1; 
	int lastStall = -1;
	//for each step K
	int i = 0; 
	while(i < K)
	{
		//search for regions
		vector<vector<int>> sects = sections(bathroom); //printSects(sects, caseNum);
		//get largest leftmost region
		vector<int> lSect = largestSect(sects, caseNum); //printv(lSect);
		//use lsect to get start and end and len
		int start = lSect.front(), end = lSect.back(), len = lSect.size(); //cout << "len: " << len << endl;
		
		if(len%2 == 1)
		{
			//cout << "odd\n";
			//cout << "lSect[len/2]: " << lSect[len/2] << endl;
			bathroom[lSect[len/2]] = 1;
			lastStall = lSect[len/2];
		}
		else //if(len%2 == 0)
		{
			//cout << "even\n";
			//cout << "lSect[(len/2)-1]: " << lSect[(len/2)-1] << endl;
			bathroom[lSect[(len/2)-1]] = 1;
			lastStall = lSect[(len/2)-1];
		}		
		if(caseNum == CURR_NUM){/*cout << "lastStall: " << lastStall << endl << endl;*/}
		//printv(bathroom, caseNum);
		i++;
	}
	//printv(bathroom, caseNum);
	vector<vector<int>> finalRegions = sections(bathroom); //printSects(finalRegions);
	//if(caseNum == CURR_NUM){cout << "lastStall: " << lastStall << endl << endl;}
	pair<int,int> lr = LR(finalRegions, lastStall);
	//cout << "Case #" << caseNum << ": " <<  max(lr.first, lr.second) << " " << min(lr.first, lr.second) << endl;
	fout << "Case #" << caseNum << ": " <<  max(lr.first, lr.second) << " " << min(lr.first, lr.second) << endl;
}
int main() {
	//ifstream sampleIn("sample.in");
	//ofstream sampleOut("sample.out");
	ifstream smallIn1("C-small-1-attempt1.in");
	ofstream smallOut1("small1.out");
	/*ifstream largeIn("B-large.in");
	ofstream largeOut("large.out");*/
	smallIn1 >> NumCases;
	int i = 0;
	while(i < NumCases)
	{
		////cout << "testcase: " << i+1 << endl;
		bathroom_stalls(smallIn1, smallOut1, i+1);
		i++;
	}
  return 0;
}