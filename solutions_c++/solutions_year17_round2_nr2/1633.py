#include <iostream>
#include <fstream>
#include <vector>
#include <string.h>
#include <math.h>
#include <algorithm>

using namespace std;

string CalculateResult();
vector<int> CalculateOrder();

int R, O, Y, G, B, V;
vector<int> colors;
int N;

int main(){
	ifstream in("input.txt");
  	ofstream out("output.txt");

  	int nRighe;
  	in >> nRighe;

  	for(int i = 0; i < nRighe; i++)
  	{
  		colors.clear();
  		in >> N >> R >> O >> Y >> G >> B >> V;
  		colors.push_back(R);
  		colors.push_back(O);
  		colors.push_back(Y);
  		colors.push_back(G);
  		colors.push_back(B);
  		colors.push_back(V);

  		string result = CalculateResult();

  		out << "Case #" << i+1 << ": " << result << endl;
  	}
  
  	return 0;
}

vector<int> CalculateOrder()
{
	vector<int> order;
	vector<int> colorsCopy;
	vector<bool> taken;

	//copy color vector
	for(int i = 0; i < 6; i++)
	{
		colorsCopy.push_back(colors[i]);
		taken.push_back(false);
	}

	//order
	for(int i = 0; i < 5; i++)
	{
		for(int j = i+1; j < 6; j++)
		{
			if(colorsCopy[i] < colorsCopy[j])
			{
				int tmp = colorsCopy[j];
				colorsCopy[j] = colorsCopy[i];
				colorsCopy[i] = tmp;
			}
		}
	}

	//create index vector
	for(int i = 0; i < 6; i++)
	{
		for(int j = 0; j < 6; j++)
		{
			if(colorsCopy[i] == colors[j] && taken[j] == false)
			{
				order.push_back(j);
				taken[j] = true;
				break;
			}
		}
		
	}

	return order;
}

string CalculateResult()
{
	vector<int> order = CalculateOrder();
	//cout << order[0] << order[1]<< order[2]<< order[3]<< order[4]<< order[5] <<endl;

	//tmp string
	string result = "";
	for(int i = 0; i < N; i++)
	{
		result += '9';
	}

	//do stuff
	int currIndex = 0;
	for(int i = 0; i < 6; i++)
	{
		for(int j = 0; j < colors[order[i]]; j++)
		{
			while(colors[order[i]] != 0)
			{
				if(result[currIndex] == '9')
				{
					result[currIndex] = order[i]+48; //ASCII logic...
					colors[order[i]]--;
					currIndex += 2;
					if(currIndex >= N)
						currIndex = currIndex % N;
				}
				else
				{
					currIndex++;
					if(currIndex >= N)
						currIndex = currIndex % N;
				}
			}
		}
	}

	//convert to letters
	for(int i = 0; i < N; i++)
	{
		if(result[i] == '0')
			result[i] = 'R';
		else if(result[i] == '1')
			result[i] = 'O';
		else if(result[i] == '2')
			result[i] = 'Y';
		else if(result[i] == '3')
			result[i] = 'G';
		else if(result[i] == '4')
			result[i] = 'B';
		else if(result[i] == '5')
			result[i] = 'V';
	}

	for(int i = 0; i < N-1; i++)
	{
		if(result[i] == result[i+1])
		{
			result = "IMPOSSIBLE";
			break;
		}
	}

	if(result[0] == result[N-1] && result != "IMPOSSIBLE")
		result = "IMPOSSIBLE";
	return result;
}