//
// Created by pierre on 08.04.17.
//

#include <iostream>

#define int long long

using namespace std;

int range[109];
double speed[109];
int inDist[109][109];
int dist[109][109];
double matrix[109][109];


int V, Q;

void kij(int tab[109][109]);
void kij(double tab[109][109]);

main()
{
  int ilez;
  cin >> ilez;
  for (int aa = 0; aa < ilez; aa++)
  {
    cin >> V >> Q;

    for (int i = 0; i < V; i++)
    {
      cin >> range[i] >> speed[i];
    }

    for (int i = 0; i < V; i++)
    {
      for (int j = 0; j < V; j++)
      {
        cin >> inDist[i][j];
      }
    }

    kij(inDist);


    for (int i = 0; i < V; i++)
    {
      for (int j = 0; j < V; j++)
      {
        if (inDist[i][j] > 0 && range[i] >= inDist[i][j])
        {
          matrix[i][j] = inDist[i][j] / speed[i];
        }
        else
        {
          matrix[i][j] = -1;
        }
      }
    }

    kij(matrix);

    cout << "Case #" << aa + 1 << ": ";

    for (int i = 0; i < Q; i++)
    {
      int a, b;
      cin >> a >> b;
      a--;
      b--;
      cout.precision(7);
      cout << fixed << matrix[a][b] << " ";
    }
    cout << endl;

  }
}


void kij(int tab[109][109])
{
  for (int k = 0; k < V; k++)
  {
    for (int i = 0; i < V; i++)
    {
      for (int j = 0; j < V; j++)
      {
        if (tab[i][k] > 0 && tab[k][j] > 0 && (tab[i][j] < 0 || tab[i][j] > tab[i][k] + tab[k][j]))
        {
          tab[i][j] = tab[i][k] + tab[k][j];
        }
      }
    }
  }
}

void kij(double tab[109][109])
{
  for (int k = 0; k < V; k++)
  {
    for (int i = 0; i < V; i++)
    {
      for (int j = 0; j < V; j++)
      {
        if (tab[i][k] > 0 && tab[k][j] > 0 && (tab[i][j] < 0 || tab[i][j] > tab[i][k] + tab[k][j]))
        {
          tab[i][j] = tab[i][k] + tab[k][j];
        }
      }
    }
  }
}
