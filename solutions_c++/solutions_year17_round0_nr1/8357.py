#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <set>
using namespace std;
int getFlip(string pan, int k)
{
  set<string> usedPan;
  usedPan.insert(pan);
  int totalStep = 0;
  string target;
  for(int i = 0; i < pan.size(); i++)
  {
  	target.push_back('+');
  }
  vector<string> currentLevel = {pan};
  while(usedPan.find(target) == usedPan.end())
  {
  	 if(pan.size() < k) return -1;
  	 vector<string> nextLevel;
  	 for(int i = 0; i < currentLevel.size(); i++)
  	 {
  	 	//cout << "level " << totalStep << " " << currentLevel[i] << endl;
  	 	string currentPan = currentLevel[i];
  	 	for(int j = 0; j <= currentPan.size() - k; j++)
  	 	{
  	 		string nextPan = currentPan;
  	 		for(int jj = 0; jj < k; jj++)
  	 		{
  	 			if(nextPan[jj + j] == '-') nextPan[jj + j] = '+';
  	 			else nextPan[jj + j] = '-';
  	 		}
  	 		if(usedPan.find(nextPan) == usedPan.end())
  	 		{
  	 			usedPan.insert(nextPan);
  	 			nextLevel.push_back(nextPan);
  	 		}
  	 	}
  	 }
  	 if(nextLevel.size() == 0) return -1;
  	 currentLevel =  nextLevel;
  	 totalStep++;    
  }
  return totalStep;
}

int main()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.out");
	int totalCase;
	fin >> totalCase;
	for(int i = 1; i <= totalCase; i++)
	{
		string cakes;
		int k;
		fin >> cakes >> k;
		fout << "Case #" << to_string(i) << ": ";
		int times = getFlip(cakes, k);
		if (times == -1) fout << "IMPOSSIBLE" << endl;
		else fout << times << endl;
	}
	return 0;
}