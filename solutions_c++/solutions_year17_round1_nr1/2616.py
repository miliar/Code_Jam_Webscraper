#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <set>
#include <map>
#include <algorithm>
#include <ctime>
using namespace std;
struct ِAdjListNode {
	int dest;
	ِAdjListNode *next;
};
struct AdjList {
	ِAdjListNode *head;
};
struct Graph {
	int v;
	AdjList *Nodes;
};
ِAdjListNode *newAdjListNode(int dest)
{
	ِAdjListNode *newNode = new ِAdjListNode;
	newNode->dest = dest;
	newNode->next = NULL;
	return newNode;
}
Graph* createGraph(int V)
{
	Graph* graph = new Graph;
	graph->v = V;

	// Create an array of adjacency lists.  Size of array will be V
	graph->Nodes = new AdjList[V + 1];

	// Initialize each adjacency list as empty by making head as NULL
	int i;
	for (i = 1; i <= V; ++i)
		graph->Nodes[i].head = NULL;

	return graph;
}
void addEdge(Graph* graph, int src, int dest)
{
	ِAdjListNode *newNode = newAdjListNode(dest);
	newNode->next = graph->Nodes[src].head;
	graph->Nodes[src].head = newNode;

	newNode = newAdjListNode(src);
	newNode->next = graph->Nodes[dest].head;
	graph->Nodes[dest].head = newNode;
}
void printGraph(Graph* graph)
{
	int v;
	for (v = 1; v < graph->v; ++v)
	{
		ِAdjListNode *pCrawl = graph->Nodes[v].head;
		cout << "Adjacency list of vertex " << v << endl << "Head";
		while (pCrawl)
		{
			cout << "->" << pCrawl->dest << " ";
			pCrawl = pCrawl->next;
		}
		cout << endl;
	}
}
vector<vector<pair<char, int> > > Grid;
int R, C;
bool fillTheGrid()
{
	bool notFound = false;
	for (int j = 0; j < R; j++)
	{
		for (int h = 0; h < C; h++)
		{
			if (Grid[j][h].first == '?')
			{
				bool flagAs = true;
				vector<pair<char, int> > founded;
				if (Grid[j][h].second == 0)
				{

					for (int m = h - 1; m >= 0; m--)
					{
						if (Grid[j][m].first != '?')
						{
							if (Grid[j][m].second == 0 || Grid[j][m].second == 1)
							{
								Grid[j][h].first = Grid[j][m].first;
								Grid[j][h].second = 1;
								Grid[j][m].second = 1;
								flagAs = false;
								break;
							}
							else
							{
								pair<char, int>ff;
								ff.first = Grid[j][m].first;
								ff.second = 1;
								founded.push_back(ff);
							}
						}
					}
					if (flagAs)
					{
						for (int m = h + 1; m < C; m++)
						{
							if (Grid[j][m].first != '?')
							{
								if (Grid[j][m].second == 0 || Grid[j][m].second == 1)
								{
									Grid[j][h].first = Grid[j][m].first;
									Grid[j][m].second = 1;
									Grid[j][m].second = 1;
									flagAs = false;

								}
								else
								{
									pair<char, int>ff;
									ff.first = Grid[j][m].first;
									ff.second = 1;
									founded.push_back(ff);
								}
								break;
							}

						}
					}
					if (flagAs)
					{
						for (int m = j + 1; m < R; m++)
						{
							if (Grid[m][h].first != '?')
							{
								if (Grid[m][h].second == 0 || Grid[m][h].second == 2)
								{
									Grid[j][h].first = Grid[m][h].first;
									Grid[j][h].second = 2;
									Grid[m][h].second = 2;
									flagAs = false;

								}
								else
								{
									pair<char, int>ff;
									ff.first = Grid[m][h].first;
									ff.second = 2;
									founded.push_back(ff);
								}
								break;
							}
						}
					}
					if (flagAs)
					{
						for (int m = j - 1; m > -1; m--)
						{
							if (Grid[m][h].first != '?')
							{
								if (Grid[m][h].second == 0 || Grid[m][h].second == 2)
								{
									Grid[j][h].first = Grid[m][h].first;
									Grid[j][h].second = 2;
									Grid[m][h].second = 2;

								}
								else
								{
									pair<char, int>ff;
									ff.first = Grid[m][h].first;
									ff.second = 2;
									founded.push_back(ff);
								}
								break;
							}
						}
					}
					if (flagAs)
					{
						if (founded.size() > 0)
						{
							Grid[j][h].first = founded[0].first;
							Grid[j][h].second = founded[0].second;
						}
						else
							notFound = true;
					}
				}
			}
		}
	}
	return notFound;
}

int main() {

	ifstream  cin; ofstream cout; 
	cin.open("A-large.in"); 
	cout.open("output.out");
	int q;
	cin >> q;
	for (int i = 1; i <= q; i++)
	{
		cin >> R >> C;
		vector<pair<string, bool> > grid;

		for (int j = 0; j < R; j++)
		{

			string temp = "";
			bool tempFlag = true;
			for (int h = 0; h < C; h++)
			{
				char f;
				cin >> f;
				temp += f;

				if (f != '?')
					tempFlag = false;
			}
			pair<string, bool> tempP;
			tempP.first = temp;
			tempP.second = tempFlag;
			grid.push_back(tempP);
		}
		for (int j = 0; j < R; j++)
		{
			if (grid[j].second)
			{
				if (j > 0)
				{
					if (grid[j - 1].second == false)
					{
						grid[j].first = grid[j - 1].first;
						grid[j].second = false;
						continue;
					}
				}
			}
			else
			{
				char theChar = '?';
				bool flagFindFirst = false;
				for (int h = 0; h < grid[j].first.length(); h++)
				{
					if (grid[j].first[h] == '?')
					{
						if (theChar == '?')
							flagFindFirst = true;
						grid[j].first[h] = theChar;
					}
					else
					{
						theChar = grid[j].first[h];
						if (flagFindFirst)
						{
							for (int t = h - 1; t >= 0; t--)
							{
								grid[j].first[t] = theChar;
							}
							flagFindFirst = false;
						}
					}
				}
			}
		}
		for (int j = 0; j < R; j++)
		{
			if (grid[j].second)
			{
				bool replaced = false;
				vector<int>fady;
				for (int t = j - 1; t >= 0; t--)
				{
					if (grid[t].second)
						fady.push_back(t);
					else
					{
						grid[j] = grid[t]; replaced = true;
						for (int l = 0; l < fady.size(); l++)
						{
							grid[fady[l]] = grid[t];
						}
						break;
					}
				}
				if (replaced == false)
				{
					for (int t = j + 1; t < R; t++)
					{
						if (grid[t].second)
							fady.push_back(t);
						else
						{
							grid[j] = grid[t]; replaced = true;
							for (int l = 0; l < fady.size(); l++)
							{
								grid[fady[l]] = grid[t];
							}
							break;
						}
					}
				}
			}
		}
		cout << "Case #" << i << ":" << endl;
		for (int j = 0; j < R; j++)
		{
			cout << grid[j].first << endl;
		}
	}
	return 0;
}
