import cv2

# カメラデバイスの設定（0は接続されている最初のカメラを指します）
cap = cv2.VideoCapture(0)

# カメラが正常に起動しているか確認
if not cap.isOpened():
    print("カメラが検出されませんでした")
    exit()

# 映像のリアルタイム表示
while True:
    ret, frame = cap.read()
    if not ret:
        print("フレームを取得できませんでした")
        break
    
    # ウィンドウにフレームを表示
    cv2.imshow("Webcam Display", frame)
    
    # "q"キーを押すとループを終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# リソースの解放
cap.release()
cv2.destroyAllWindows()
