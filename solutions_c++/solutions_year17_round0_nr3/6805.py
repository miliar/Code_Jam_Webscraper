#include<iostream>
#include<string>
#include<vector>
using namespace std;

struct pairofnums
{
	int x, y;
};

int max(pairofnums p)
{
	return p.x > p.y ? p.x : p.y;
}

int min(pairofnums p)
{
	return p.x < p.y ? p.x : p.y;
}

int smallestval(vector<int> vc)
{
	int smallest = vc[0];
	for (int i = 0; i < (int)vc.size(); i++)
	{
		if (vc[i] < smallest)
		{
			smallest = vc[i];
		}
	}
	return smallest;
}

int main()
{
	int testcases;
//	testcases = 5;
	cin >> testcases;
	int stalllen, persons;
	bool foundleft = false;
	bool foundright = false;
	for (int t = 1; t <= testcases; t++)
	{
//		stalllen = 6;
//		persons = 2;
		cin >> stalllen;
		cin >> persons;
		
		pairofnums* stallpairs = new pairofnums[stalllen];
		string stalls(stalllen, '.');	// create a string of stalls length and all as dots;

		vector<int> minindicestoplace;
		vector<int> maxindicestoplace;
		
		int currentindex;
		int lastindex;
		for (int j = 0; j < persons; j++) // for every person
		{
			minindicestoplace.clear();
			maxindicestoplace.clear();

			for (currentindex = 0; currentindex < stalllen; currentindex++)
			{
				 foundleft = false;
				 foundright = false;
				if (stalls[currentindex] != 'O')
				{
					stallpairs[currentindex].x = 0;
					stallpairs[currentindex].y = 0;

					for (int m = currentindex - 1, l = currentindex + 1; m >= 0 || l < stalllen; m--, l++)//calculating pair values for every non-occupied index
					{
						if (m >= 0 && !foundleft )
						{
							// for finding Ls
							if (stalls[m] != 'O')
							{
								stallpairs[currentindex].x++;
							}
							else
							{
								foundleft = true;
							}
						}

						if (l < stalllen && !foundright)
						{
							// for finding Rs
							if (stalls[l] != 'O')
							{
								stallpairs[currentindex].y++;
							}
							else
							{
								foundright = true;
							}
						}
					}
				}
			}
			//
			currentindex = 0;
			int minvalue;
			while (true)	// will end when we find the first possible index
			{
				if (stalls[currentindex] != 'O')	// the first vacant space
				{
					minvalue = min(stallpairs[currentindex]);// saving the minimum min value
					minindicestoplace.push_back(currentindex++);// and tha index upon which that value was
					break;	// leave the loop
				}
				else
					currentindex++;
			}
			for (int i = currentindex; i < stalllen; i++)	// from that point till end
			{
				if (stalls[i] != 'O')	// onward from the first possible index
				{
					if (min(stallpairs[i]) > minvalue)	// having maximul min-value
					{
						currentindex = i;	// index on the original string
						minindicestoplace.clear();
						minindicestoplace.push_back(currentindex);
						minvalue = min(stallpairs[i]);
					}
					else
						if (min(stallpairs[i]) == minvalue)
						{
							minindicestoplace.push_back(i);// if we have multiple indices with same min
						}
				}
			}
			int maxvalue;
			if (minindicestoplace.size() > 1)// when we find more than one spots
			{
				maxindicestoplace.push_back(minindicestoplace[0]);// getting the first value from mins array to maxs array
				maxvalue = max(stallpairs[maxindicestoplace[0]]);	// setting the maxvalue
				for (int i = 1; i < (int)minindicestoplace.size(); i++)	// upto the every shortlisted index
				{
					if (max(stallpairs[minindicestoplace[i]]) > maxvalue)
					{
						maxindicestoplace.clear();	// have to clear the old recorded multiple values
						maxvalue = max(stallpairs[minindicestoplace[i]]);
						maxindicestoplace.push_back(minindicestoplace[i]);
					}else
						if (max(stallpairs[minindicestoplace[i]]) == maxvalue)
						{
							maxindicestoplace.push_back(minindicestoplace[i]);
						}
				}
				if (maxindicestoplace.size() > 1)
				{
					lastindex = smallestval(maxindicestoplace);
					stalls[lastindex] = 'O';
				}
				else
				{
					lastindex = maxindicestoplace[0];
					stalls[lastindex] = 'O';
				}
			}
			else 
			{
				lastindex = minindicestoplace[0];
				stalls[lastindex] = 'O';
			}
		}
		cout << "Case #" << t << ": " << max(stallpairs[lastindex]) << " " << min(stallpairs[lastindex]) << endl;
		delete[] stallpairs;
	}
	return 0;
}